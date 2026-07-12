#!/usr/bin/env python3
"""A minimal HTTPS CONNECT proxy that forwards ONLY to an allowlist of hosts.

Runs as a sidecar on the internal egress network. The extractor container has
no other route to the internet, so this is the single choke point: it permits
`CONNECT` tunnels to Anthropic hosts and refuses everything else with 403. It
never inspects tunnel contents (TLS), it only gates the destination host.

Stdlib only — the extractor image ships no third-party Python.
"""
from __future__ import annotations

import os
import select
import socket
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ALLOWED_HOSTS = frozenset(
    h.strip().lower() for h in os.environ.get("ALLOWED_HOSTS", "").split(",") if h.strip()
)
PORT = int(os.environ.get("PROXY_PORT", "8888"))


def _host_allowed(host: str) -> bool:
    host = host.lower()
    return host in ALLOWED_HOSTS


class Proxy(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):  # keep stderr quiet
        pass

    def do_CONNECT(self):  # noqa: N802
        host, _, port = self.path.partition(":")
        port = int(port or 443)
        if not _host_allowed(host):
            self.send_error(403, "host not on Anthropic allowlist")
            return
        try:
            upstream = socket.create_connection((host, port), timeout=30)
        except OSError:
            self.send_error(502, "upstream connect failed")
            return
        self.send_response(200, "Connection Established")
        self.end_headers()
        self._tunnel(self.connection, upstream)

    def _reject_plain(self):
        # We only allow HTTPS CONNECT tunnels; refuse plain HTTP proxying.
        self.send_error(403, "only HTTPS CONNECT to allowlisted hosts is permitted")

    do_GET = do_POST = do_PUT = do_DELETE = do_HEAD = do_OPTIONS = _reject_plain

    @staticmethod
    def _tunnel(client: socket.socket, upstream: socket.socket) -> None:
        socks = [client, upstream]
        try:
            while True:
                readable, _, err = select.select(socks, [], socks, 60)
                if err:
                    break
                for s in readable:
                    data = s.recv(65536)
                    if not data:
                        return
                    (upstream if s is client else client).sendall(data)
        except OSError:
            pass
        finally:
            for s in (client, upstream):
                try:
                    s.close()
                except OSError:
                    pass


def main() -> None:
    if not ALLOWED_HOSTS:
        raise SystemExit("refusing to start: ALLOWED_HOSTS is empty")
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Proxy)
    server.daemon_threads = True
    threading.current_thread().name = "egress-proxy"
    server.serve_forever()


if __name__ == "__main__":
    main()

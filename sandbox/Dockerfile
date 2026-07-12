# Extraction image: the smallest thing that can run `claude -p` and our two
# stdlib Python scripts. Deliberately spartan — no git, no ssh, no curl, no
# compilers, no build tools. The less that is in here, the less an injected
# model could reach even if it had tools (it does not).
#
# NOTE: `@anthropic-ai/claude-code` is the Claude Code *CLI*, not the `anthropic`
# Python SDK. This image installs no API SDK and reads no API key; auth comes
# from the read-only subscription credentials mounted at runtime.
FROM node:20-slim

# python3 for entrypoint.py (extractor) and egress_proxy.py (sidecar). Pinned
# CLI version for reproducibility. Clean apt lists to keep the image minimal.
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && npm install -g @anthropic-ai/claude-code@2.1.207 \
    && npm cache clean --force

# Non-root user; matches --user 10001:10001 in pipeline/sandbox.py.
RUN groupadd -g 10001 extractor && useradd -u 10001 -g 10001 -m extractor

COPY entrypoint.py /opt/entrypoint.py
COPY egress_proxy.py /opt/egress_proxy.py
RUN chmod 0555 /opt/entrypoint.py /opt/egress_proxy.py

USER 10001:10001
ENV HOME=/tmp/home
WORKDIR /tmp

# Default: run the extractor. The proxy sidecar overrides --entrypoint.
ENTRYPOINT ["python3", "/opt/entrypoint.py"]

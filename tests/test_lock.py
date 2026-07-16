"""The run lock must reclaim a stale lock (dead owner) but respect a live one.

A run that is killed mid-flight leaves state/.lock behind. Before the reclaim
logic, that stale file wedged every subsequent run ("another run holds the
lock") — which is exactly what silently stalled the nightly job for days.
"""
from __future__ import annotations

import os

import pytest

from pipeline import run


@pytest.fixture
def lock_path(tmp_path, monkeypatch):
    p = tmp_path / ".lock"
    monkeypatch.setattr(run, "LOCK_PATH", p)
    monkeypatch.setattr(run.config, "STATE_DIR", tmp_path)
    return p


def test_acquires_when_absent(lock_path):
    with run._Lock():
        assert lock_path.exists()
        assert lock_path.read_text().strip() == str(os.getpid())
    assert not lock_path.exists()  # released on exit


def test_reclaims_stale_lock(lock_path):
    # A dead pid: 2**31-1 is far above any real pid on Linux.
    dead_pid = 2**31 - 1
    assert not run._pid_alive(dead_pid)
    lock_path.write_text(f"{dead_pid}\n")
    with run._Lock():
        assert lock_path.read_text().strip() == str(os.getpid())
    assert not lock_path.exists()


def test_reclaims_garbage_lock(lock_path):
    lock_path.write_text("not-a-pid\n")
    with run._Lock():  # unparseable owner is treated as stale
        assert lock_path.read_text().strip() == str(os.getpid())


def test_refuses_when_owner_alive(lock_path):
    # This process is alive and is not us-as-owner only because we write our own
    # pid; use the parent pid, which is also alive, to stand in for a live owner.
    live_pid = os.getppid()
    assert run._pid_alive(live_pid)
    lock_path.write_text(f"{live_pid}\n")
    with pytest.raises(SystemExit) as exc:
        with run._Lock():
            pass
    assert exc.value.code == 0  # a live owner is a benign skip, not a failure
    assert lock_path.read_text().strip() == str(live_pid)  # left intact

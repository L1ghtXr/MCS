import os
import tempfile
from pathlib import Path


def get_log_path(filename="stress_test.log"):
    cwd = Path.cwd()
    try:
        probe = cwd / f".mcs_write_{os.getpid()}"
        probe.touch()
        probe.unlink()
        return cwd / filename
    except OSError:
        pass
    return Path(tempfile.gettempdir()) / filename


def ensure_dir(path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

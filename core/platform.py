import os
import platform
from enum import Enum
from functools import lru_cache


class OS(str, Enum):
    LINUX = "linux"
    WINDOWS = "windows"
    MACOS = "macos"
    FREEBSD = "freebsd"
    TERMUX = "termux"
    ANDROID = "android"
    WSL = "wsl"
    UNKNOWN = "unknown"


def _is_termux():
    prefix = os.environ.get("PREFIX", "")
    if "com.termux" in prefix:
        return True
    try:
        return os.path.isdir("/data/data/com.termux")
    except OSError:
        return False


def _is_android():
    return "ANDROID_ROOT" in os.environ or "ANDROID_DATA" in os.environ


def _is_wsl():
    if os.environ.get("WSL_DISTRO_NAME") or os.environ.get("WSL_INTEROP"):
        return True
    try:
        with open("/proc/version", "r", encoding="utf-8", errors="ignore") as f:
            return "microsoft" in f.read().lower()
    except OSError:
        return False


def _is_docker():
    try:
        if os.path.exists("/.dockerenv"):
            return True
    except OSError:
        pass
    try:
        with open("/proc/1/cgroup", "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
            return "docker" in c or "kubepods" in c
    except OSError:
        return False


@lru_cache(maxsize=1)
def detect_os():
    try:
        system = platform.system().lower()
    except Exception:
        return OS.UNKNOWN

    if system == "windows":
        return OS.WINDOWS
    if system == "darwin":
        return OS.MACOS
    if system == "freebsd":
        return OS.FREEBSD
    if system == "linux":
        if _is_termux():
            return OS.TERMUX
        if _is_wsl():
            return OS.WSL
        if _is_android():
            return OS.ANDROID
        return OS.LINUX
    return OS.UNKNOWN


@lru_cache(maxsize=1)
def is_docker():
    return _is_docker()


@lru_cache(maxsize=1)
def get_platform_info():
    return {
        "os": detect_os().value,
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "docker": is_docker(),
    }


def is_windows():
    return detect_os() == OS.WINDOWS


def is_posix():
    return os.name == "posix"


def is_mobile():
    return detect_os() in (OS.TERMUX, OS.ANDROID)

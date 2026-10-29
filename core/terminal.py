import os
import sys

from colorama import init as colorama_init

from .platform import OS, detect_os


def init_terminal():
    colorama_init(autoreset=True)

    if detect_os() == OS.WINDOWS:
        try:
            os.system("")
        except Exception:
            pass
        for stream in (sys.stdout, sys.stderr):
            if hasattr(stream, "reconfigure"):
                try:
                    stream.reconfigure(encoding="utf-8", errors="replace")
                except Exception:
                    pass


def set_title(title):
    if detect_os() == OS.WINDOWS:
        try:
            import ctypes

            ctypes.windll.kernel32.SetConsoleTitleW(title)
            return
        except Exception:
            pass
    try:
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()
    except Exception:
        pass


def clear_screen():
    if detect_os() == OS.WINDOWS:
        try:
            os.system("cls")
            return True
        except Exception:
            pass
    try:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        return True
    except Exception:
        return False

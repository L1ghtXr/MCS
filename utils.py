import logging
import socket
import struct
import time

from colorama import Fore, Style

from core.filesystem import get_log_path

_handlers = [logging.StreamHandler()]
try:
    _handlers.append(logging.FileHandler(str(get_log_path()), encoding="utf-8"))
except OSError:
    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=_handlers,
)
log = logging.getLogger("mcs")


def ok(msg):
    log.info(f"{Fore.GREEN}{msg}{Style.RESET_ALL}")


def warn(msg):
    log.warning(f"{Fore.YELLOW}{msg}{Style.RESET_ALL}")


def err(msg):
    log.error(f"{Fore.RED}{msg}{Style.RESET_ALL}")


def ask_ip():
    while True:
        ip = input(f"{Fore.CYAN}Target IP/host: {Style.RESET_ALL}").strip()
        if ip:
            return ip
        warn("IP/host required.")


def ask_port():
    while True:
        try:
            p = int(input(f"{Fore.CYAN}Target port: {Style.RESET_ALL}").strip())
            if 1 <= p <= 65535:
                return p
        except ValueError:
            pass
        warn("Port must be 1-65535.")


def ask_duration():
    while True:
        try:
            d = int(input(f"{Fore.CYAN}Duration seconds: {Style.RESET_ALL}").strip())
            if d >= 1:
                return d
        except ValueError:
            pass
        warn("Duration must be >= 1.")


def write_varint(value):
    out = b""
    while True:
        b = value & 0x7F
        value >>= 7
        if value:
            out += bytes([b | 0x80])
        else:
            out += bytes([b])
            return out


def read_varint(sock):
    num = 0
    shift = 0
    while True:
        b = sock.recv(1)
        if not b:
            raise ConnectionError("EOF")
        val = b[0]
        num |= (val & 0x7F) << shift
        if not (val & 0x80):
            return num
        shift += 7
        if shift > 35:
            raise ValueError("VarInt too big")


def build_handshake(host, port, next_state, protocol=764):
    host_b = host.encode()
    payload = b""
    payload += write_varint(0x00)
    payload += write_varint(protocol)
    payload += write_varint(len(host_b)) + host_b
    payload += struct.pack(">H", port)
    payload += write_varint(next_state)
    return write_varint(len(payload)) + payload


def build_status_request():
    payload = write_varint(0x00)
    return write_varint(len(payload)) + payload


def build_ping(ms):
    payload = write_varint(0x01) + struct.pack(">q", ms)
    return write_varint(len(payload)) + payload


def build_login_start(username):
    ub = username.encode()
    payload = write_varint(0x00) + write_varint(len(ub)) + ub
    return write_varint(len(payload)) + payload

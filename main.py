import asyncio

from colorama import Fore, Style

from core.levels import pick_level
from core.platform import OS, detect_os, get_platform_info
from core.terminal import init_terminal, set_title
from modules import http_methods, tcp_methods, udp_methods
from utils import ask_duration, ask_ip, ask_port, err, ok


def build_banner():
    info = get_platform_info()
    label = info["os"]
    if info["docker"]:
        label += " (docker)"
    return f"""
{Fore.CYAN}{Style.BRIGHT}
███╗   ███╗  ██████╗███████╗
████╗ ████║ ██╔════╝██╔════╝
██╔████╔██║ ██║     ███████╗
██║╚██╔╝██║ ██║     ╚════██║
██║ ╚═╝ ██║ ╚██████╗███████║
╚═╝     ╚═╝  ╚═════╝╚══════╝
{Style.RESET_ALL}
  {Fore.WHITE}{Style.BRIGHT}MCS — Minecraft Stress Test{Style.RESET_ALL}
  {Fore.LIGHTBLACK_EX}Minecraft server testing utility{Style.RESET_ALL}

  {Fore.LIGHTBLACK_EX}────────────────────────────────────────────{Style.RESET_ALL}

  {Fore.CYAN}Version {Fore.WHITE} : 1.0.0
  {Fore.CYAN}Platform{Fore.WHITE} : {label}
  {Fore.CYAN}Mode    {Fore.WHITE} : {Fore.YELLOW}Unrestricted
  {Fore.CYAN}Author  {Fore.WHITE} : L1ghtXr
  {Fore.CYAN}Contrib {Fore.WHITE} : DevBrezz

  {Fore.LIGHTBLACK_EX}────────────────────────────────────────────{Style.RESET_ALL}

  {Fore.LIGHTBLACK_EX}Open-source project • Built for Minecraft testing{Style.RESET_ALL}
"""


def handle_unknown_platform():
    if detect_os() == OS.UNKNOWN:
        print(f"{Fore.YELLOW}MCS")
        print("Unsupported or unknown platform detected.")
        print(f"Running in compatibility mode...{Style.RESET_ALL}\n")


def main_menu(ip, port):
    print(f"""
{Fore.CYAN}{Style.BRIGHT}━━━ MAIN MENU ━━━{Style.RESET_ALL}
  {Fore.LIGHTBLACK_EX}Target: {ip}:{port}{Style.RESET_ALL}
  {Fore.WHITE}1.{Style.RESET_ALL} Layer 4 — UDP
  {Fore.WHITE}2.{Style.RESET_ALL} Layer 4 — TCP
  {Fore.WHITE}3.{Style.RESET_ALL} Layer 7 — HTTP
  {Fore.WHITE}0.{Style.RESET_ALL} Exit
""")


def udp_menu():
    print(f"""
{Fore.CYAN}{Style.BRIGHT}━━━ LAYER 4 UDP ━━━{Style.RESET_ALL}
  {Fore.WHITE}1.{Style.RESET_ALL} UDP Spam
  {Fore.WHITE}2.{Style.RESET_ALL} UDP Handshake Flood
  {Fore.WHITE}3.{Style.RESET_ALL} UDP Query Flood
  {Fore.WHITE}0.{Style.RESET_ALL} Back
""")


def tcp_menu():
    print(f"""
{Fore.CYAN}{Style.BRIGHT}━━━ LAYER 4 TCP ━━━{Style.RESET_ALL}
  {Fore.WHITE}1.{Style.RESET_ALL} TCP Connect Flood
  {Fore.WHITE}2.{Style.RESET_ALL} TCP Join Flood
  {Fore.WHITE}3.{Style.RESET_ALL} TCP Login Flood
  {Fore.WHITE}0.{Style.RESET_ALL} Back
""")


def http_menu():
    print(f"""
{Fore.CYAN}{Style.BRIGHT}━━━ LAYER 7 HTTP ━━━{Style.RESET_ALL}
  {Fore.WHITE}1.{Style.RESET_ALL} HTTP Status Flood
  {Fore.WHITE}2.{Style.RESET_ALL} HTTP Query Flood
  {Fore.WHITE}0.{Style.RESET_ALL} Back
""")


async def run_udp(ip, port):
    udp_menu()
    c = input(f"{Fore.CYAN}Select: {Style.RESET_ALL}").strip()
    if c == "0":
        return
    if c not in {"1", "2", "3"}:
        err("Invalid choice.")
        return
    level = pick_level()
    if level is None:
        return
    dur = ask_duration()
    rate = level["udp"]
    if c == "1":
        await udp_methods.udp_spam(ip, port, dur, rate)
    elif c == "2":
        await udp_methods.udp_handshake_flood(ip, port, dur, rate)
    elif c == "3":
        await udp_methods.udp_query_flood(ip, port, dur, rate)


async def run_tcp(ip, port):
    tcp_menu()
    c = input(f"{Fore.CYAN}Select: {Style.RESET_ALL}").strip()
    if c == "0":
        return
    if c not in {"1", "2", "3"}:
        err("Invalid choice.")
        return
    level = pick_level()
    if level is None:
        return
    dur = ask_duration()
    rate = level["tcp"]
    if c == "1":
        await tcp_methods.tcp_connect_flood(ip, port, dur, rate)
    elif c == "2":
        await tcp_methods.tcp_join_flood(ip, port, dur, rate)
    elif c == "3":
        await tcp_methods.tcp_login_flood(ip, port, dur, rate)


async def run_http(ip, port):
    http_menu()
    c = input(f"{Fore.CYAN}Select: {Style.RESET_ALL}").strip()
    if c == "0":
        return
    if c not in {"1", "2"}:
        err("Invalid choice.")
        return
    scheme = input(
        f"{Fore.CYAN}Scheme (http/https, default http): {Style.RESET_ALL}"
    ).strip().lower() or "http"
    if scheme not in ("http", "https"):
        err("Invalid scheme.")
        return
    path = input(f"{Fore.CYAN}Path (default /): {Style.RESET_ALL}").strip() or "/"
    if not path.startswith("/"):
        path = "/" + path
    url = f"{scheme}://{ip}:{port}{path}"
    level = pick_level()
    if level is None:
        return
    dur = ask_duration()
    rate = level["http"]
    if c == "1":
        await http_methods.http_status_flood(url, dur, rate)
    elif c == "2":
        await http_methods.http_query_flood(url, dur, rate)


async def main():
    init_terminal()
    set_title("MCS Minecraft Stress Test")
    print(build_banner())
    handle_unknown_platform()

    ip = ask_ip()
    port = ask_port()
    input(f"{Fore.LIGHTBLACK_EX}Press Enter to open Main Menu...{Style.RESET_ALL}")

    while True:
        main_menu(ip, port)
        c = input(f"{Fore.CYAN}Select: {Style.RESET_ALL}").strip()
        if c == "1":
            await run_udp(ip, port)
        elif c == "2":
            await run_tcp(ip, port)
        elif c == "3":
            await run_http(ip, port)
        elif c == "0":
            ok("Exiting.")
            return
        else:
            err("Invalid choice.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Interrupted.{Style.RESET_ALL}")
    except SystemExit:
        raise

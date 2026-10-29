# ⚡ MCS — Minecraft Server Stress Testing Toolkit

```text
███╗   ███╗ ██████╗███████╗
████╗ ████║██╔════╝██╔════╝
██╔████╔██║██║     ███████╗
██║╚██╔╝██║██║     ╚════██║
██║ ╚═╝ ██║╚██████╗███████║
╚═╝     ╚═╝ ╚═════╝╚══════╝

Minecraft Server Stress Testing Toolkit
             Developed by DevBrezz
```

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20Termux-blue.svg)](#-platform)
[![Developer](https://img.shields.io/badge/developer-DevBrezz-purple.svg)](#-developer)

> **MCS is designed for authorized Minecraft server stress and resilience testing. Only test servers you own or have explicit permission to test.**

## 📖 Overview

MCS is a Minecraft server stress-testing toolkit designed to help server owners and developers evaluate server behavior under controlled network and application load.

It can be used to:

- Evaluate server capacity.
- Identify performance bottlenecks.
- Test connection handling.
- Test protocol handling.
- Evaluate rate limiting and protection systems.
- Measure server stability under increasing load.
- Perform controlled development and staging tests.
- Help determine safe server capacity limits.

## ✨ Features

### Layer 4 — UDP

| Method | Description |
|---|---|
| `UDP SPAM` | Tests UDP packet handling under increased traffic. |
| `UDP HANDSHAKE FLOOD` | Tests handshake processing capacity. |
| `UDP QUERY FLOOD` | Tests UDP query handling and response capacity. |

### Layer 4 — TCP

| Method | Description |
|---|---|
| `TCP CONNECT FLOOD` | Tests TCP connection handling capacity. |
| `TCP JOIN FLOOD` | Tests connection/join processing behavior. |
| `TCP LOGIN FLOOD` | Tests login processing under increased connection load. |

### Layer 7 — HTTP

| Method | Description |
|---|---|
| `HTTP STATUS FLOOD` | Tests HTTP status endpoint handling. |
| `HTTP QUERY FLOOD` | Tests HTTP query/request handling. |

## 🎚️ Stress Levels

| Level | Name | Purpose |
|---:|---|---|
| `1` | 🟢 LOW | Basic smoke and compatibility testing |
| `2` | 🟡 MEDIUM | Normal performance testing |
| `3` | 🟠 HIGH | High-load capacity testing |
| `4` | 🔴 CRITICAL | Controlled maximum-capacity testing |

The level number does **not** represent a guaranteed packet-per-second value. Actual traffic depends on network bandwidth, CPU, server software, configuration, latency, firewall/rate limits, operating system, and MCS configuration.

Always start at **LOW** and increase gradually.

## ⚙️ How It Works

```text
                    ┌──────────────────┐
                    │   MCS Controller │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Select Test      │
                    │ Method + Level   │
                    └────────┬─────────┘
                             │
                  ┌──────────┼──────────┐
                  ▼          ▼          ▼
                UDP         TCP        HTTP
                  │          │          │
                  └──────────┼──────────┘
                             ▼
                    ┌──────────────────┐
                    │ Minecraft Server │
                    └────────┬─────────┘
                             │
                             ▼
                    Monitor Performance
                             │
                             ▼
                    Analyze Test Results
```

During testing, administrators can monitor CPU, RAM, network throughput, latency, connection count, timeouts, errors, tick performance, and overall stability.

## 🖥️ Platform

MCS is intended for environments such as:

- Linux
- Windows
- Termux / Android
- VPS
- Dedicated servers
- Local development environments
- Minecraft testing laboratories

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/DevBrezz/MCS.git
cd MCS
```

Install the dependencies required by the current project build, then start MCS using its configured entry point.

### Termux

```bash
pkg update
pkg upgrade
pkg install git
git clone https://github.com/DevBrezz/MCS.git
cd MCS
```

## 🧪 Recommended Testing Procedure

Use a dedicated testing or staging server.

1. Prepare the Minecraft test server and monitoring.
2. Start with `LOW`.
3. Observe CPU, RAM, network, latency, connections, errors, and TPS/tick performance.
4. Increase gradually: `LOW → MEDIUM → HIGH → CRITICAL`.
5. Stop immediately if the server becomes unstable.

## 📊 Example Test Report

```text
========================================
           MCS TEST REPORT
========================================

Target:        Minecraft Test Server
Method:        TCP LOGIN FLOOD
Level:         MEDIUM
Duration:      60 seconds

CPU:           XX%
RAM:           XX%
Network:       XX Mbps
Latency:       XX ms
Connections:   XXX
Errors:        XX
Timeouts:      XX

Result:        STABLE
========================================
```

## 🛡️ Responsible Usage

MCS is intended for:

- Your own Minecraft server.
- Your own VPS.
- Local testing environments.
- Development servers.
- Staging environments.
- Authorized security/performance assessments.

Do **not** use MCS against systems you do not own or have permission to test.

Unauthorized traffic generation can cause service disruption and may violate laws, provider policies, or terms of service.

**You are responsible for how you use this software.**

## 🤝 Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidelines.

## 📜 License

MCS is released under the **MIT License**. See [`LICENSE`](LICENSE).

## 👨‍💻 Developer

**DevBrezz**

Minecraft tooling • Server testing • Development

## ⚠️ Disclaimer

MCS is provided for legitimate testing, development, research, and authorized security/performance assessment.

The developer does not authorize or encourage unauthorized disruption of third-party systems.

**Only test systems you own or have explicit permission to test.**

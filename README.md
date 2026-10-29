# ⚡ MCS — Minecraft Server Stress Testing Toolkit

<p align="center">
  <img src="https://img.shields.io/badge/Minecraft-Server%20Testing-green?style=for-the-badge" alt="Minecraft">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Termux-lightgrey?style=for-the-badge" alt="Platform">
</p>

<p align="center">

```text
███╗   ███╗ ██████╗███████╗
████╗ ████║██╔════╝██╔════╝
██╔████╔██║██║     ███████╗
██║╚██╔╝██║██║     ╚════██║
██║ ╚═╝ ██║╚██████╗███████║
╚═╝     ╚═╝ ╚═════╝╚══════╝

      Minecraft Server Stress Testing Toolkit
                 by L1ghtXr
          Contributions by DevBrezz
```

</p>

> **MCS is intended for authorized Minecraft server stress, resilience, and performance testing. Only test systems you own or have explicit permission to test.**

---

## 📖 Overview

**MCS** is a Minecraft-focused stress-testing toolkit designed for controlled testing of server behavior under increased network and application load.

It can help server owners and developers:

- Evaluate server capacity.
- Identify performance bottlenecks.
- Test connection and protocol handling.
- Validate rate-limiting and protection configurations.
- Observe server behavior under controlled load.
- Compare performance between configurations.
- Perform development and staging resilience tests.

MCS is designed for **authorized testing**, not unauthorized disruption of third-party infrastructure.

---

## ✨ Features

### Layer 4 — UDP

| Method | Purpose |
|---|---|
| `UDP SPAM` | Tests UDP packet handling under increased traffic. |
| `UDP HANDSHAKE FLOOD` | Tests handshake processing behavior. |
| `UDP QUERY FLOOD` | Tests UDP query handling and response behavior. |

### Layer 4 — TCP

| Method | Purpose |
|---|---|
| `TCP CONNECT FLOOD` | Tests TCP connection handling capacity. |
| `TCP JOIN FLOOD` | Tests join/connection processing behavior. |
| `TCP LOGIN FLOOD` | Tests login processing under increased connection load. |

### Layer 7 — HTTP

| Method | Purpose |
|---|---|
| `HTTP STATUS FLOOD` | Tests HTTP status endpoint handling. |
| `HTTP QUERY FLOOD` | Tests HTTP query/request handling. |

> The exact available methods depend on the current project build and configuration.

---

## 🎚️ Stress Levels

MCS uses four logical stress levels:

| Level | Classification | Intended Use |
|:---:|---|---|
| `1` | 🟢 **LOW** | Smoke testing and basic validation |
| `2` | 🟡 **MEDIUM** | Normal performance testing |
| `3` | 🟠 **HIGH** | High-load capacity testing |
| `4` | 🔴 **CRITICAL** | Controlled limit/boundary testing |

### Important

A stress level is a **classification**, not a guaranteed PPS/RPS value.

Actual traffic depends on the test method, configuration, network, CPU, bandwidth, latency, server software, firewall, rate limits, and other infrastructure factors.

**Recommended progression:**

```text
LOW → MEDIUM → HIGH → CRITICAL
```

Start low and increase gradually while monitoring the server.

---

## ⚙️ How It Works

At a high level, MCS follows this workflow:

```text
                 ┌────────────────────┐
                 │    MCS Controller  │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Select Method      │
                 │ + Stress Level     │
                 └─────────┬──────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
             UDP          TCP          HTTP
              │            │            │
              └────────────┼────────────┘
                           ▼
                 ┌────────────────────┐
                 │ Minecraft Server   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Observe Metrics    │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Analyze Results    │
                 └────────────────────┘
```

During an authorized test, operators should monitor:

- CPU utilization
- Memory utilization
- Network throughput
- Latency
- Connection behavior
- Timeout/error rates
- Server tick performance
- Overall stability

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/L1ghtXr/MCS.git
cd MCS
```

Install the dependencies required by the current project build.

For Node.js projects:

```bash
npm install
```

For Python projects:

```bash
pip install -r requirements.txt
```

> Use the dependency and start commands that match the runtime files included in your release.

---

## 📱 Termux

MCS can be used in a Termux testing environment when the required runtime is supported by the current build.

Install Git:

```bash
pkg update
pkg upgrade
pkg install git
```

Clone the repository:

```bash
git clone https://github.com/L1ghtXr/MCS.git
cd MCS
```

Install the project's required runtime and dependencies, then launch MCS using the configured entry point.

---

## 🧪 Recommended Testing Workflow

### 1. Prepare a dedicated test server

Prefer:

- Local Minecraft server
- Development server
- Staging server
- Dedicated test VPS

### 2. Start at LOW

Run a short, low-intensity test and establish a baseline.

### 3. Monitor the server

Track:

```text
CPU
RAM
Network
Latency
Connections
Timeouts
Errors
TPS / Tick Performance
```

### 4. Increase gradually

```text
LOW
  ↓
MEDIUM
  ↓
HIGH
  ↓
CRITICAL
```

Stop the test if the environment becomes unstable or normal users/services are affected.

---

## 📊 Example Test Report

```text
========================================
             MCS TEST REPORT
========================================

Target:        Authorized Test Server
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

Keep test reports so different server configurations can be compared.

---

## 🛡️ Responsible Use

MCS is intended for:

- Servers you own.
- Infrastructure you administer.
- Local testing environments.
- Development/staging environments.
- Authorized security or performance assessments.

Do **not** use MCS against systems without permission.

Unauthorized traffic generation can cause service disruption and may violate laws, hosting-provider policies, or terms of service.

**The user is responsible for ensuring every test is authorized.**

---

## 🧠 Best Practices

- Start with the lowest stress level.
- Use a dedicated testing environment whenever possible.
- Monitor the server continuously.
- Increase load gradually.
- Change one major variable at a time.
- Record CPU, memory, network, and latency results.
- Stop testing when instability appears.
- Never test third-party infrastructure without explicit authorization.

---

## 🤝 Contributing

Contributions are welcome.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting changes.

### Project Credits

- **Original project / primary developer:** **L1ghtXr**
- **Contributor:** **DevBrezz**

All contributors are expected to follow the project's responsible-use guidelines.

---

## 📜 License

MCS is distributed under the **MIT License**.

See [`LICENSE`](LICENSE) for the complete license text.

---

## 👨‍💻 Credits

### L1ghtXr
Original developer and project creator.

### DevBrezz
Contributor and project improvements/documentation.

---

## ⚠️ Disclaimer

MCS is provided for legitimate testing, development, research, and authorized performance/resilience assessment.

The project does not authorize or encourage unauthorized disruption of third-party systems.

**Only test systems you own or have explicit permission to test.**

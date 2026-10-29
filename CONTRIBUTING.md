# Contributing to MCS

Thank you for contributing to **MCS**.

MCS is originally created and maintained by **L1ghtXr**, with contributions from **DevBrezz** and the wider community.

We welcome improvements to reliability, compatibility, documentation, testing, and developer experience.

---

## 📋 Contribution Guidelines

Before submitting a contribution, please make sure that it:

- Has a clear purpose.
- Does not intentionally introduce malicious functionality.
- Does not target unauthorized third-party infrastructure.
- Does not expose credentials, secrets, or private information.
- Does not unnecessarily break existing functionality.
- Includes documentation when appropriate.
- Has been tested in an authorized environment.

---

## 🐛 Bug Reports

When reporting a bug, provide:

1. Operating system
2. Runtime/version
3. MCS version or commit
4. Steps to reproduce
5. Expected behavior
6. Actual behavior
7. Relevant logs or error messages

Example:

```text
OS: Linux
Runtime: <version>
MCS Version: <version>

Problem:
Describe the issue.

Steps:
1. Start MCS
2. Select the affected method
3. Run the authorized test
4. Observe the problem

Expected:
Describe the expected result.

Actual:
Describe what actually happened.
```

Please remove credentials, IP addresses, tokens, or other private information before posting logs.

---

## 💡 Feature Requests

Feature requests should explain:

- What problem the feature solves.
- Why it would be useful.
- How the feature should behave.
- Whether it affects existing functionality.
- Any compatibility considerations.

---

## 🔧 Pull Requests

Recommended workflow:

```text
1. Fork the repository
2. Create a feature/fix branch
3. Make your changes
4. Test your changes
5. Update documentation if necessary
6. Commit your changes
7. Open a Pull Request
```

Recommended branch names:

```text
feature/<name>
fix/<name>
docs/<name>
refactor/<name>
test/<name>
```

Examples:

```text
feature/improved-monitoring
fix/tcp-timeout
docs/update-readme
refactor/config-loader
test/protocol-handling
```

---

## 📝 Commit Messages

Use concise and descriptive commit messages.

Examples:

```text
feat: add server monitoring
fix: handle connection timeout
docs: improve installation guide
refactor: simplify configuration loader
test: add protocol tests
```

---

## 🧪 Testing Requirements

Contributors should test changes before opening a Pull Request.

Use only authorized environments, such as:

- Local Minecraft servers
- Development servers
- Staging servers
- Dedicated test infrastructure
- Systems where explicit testing permission has been granted

Do not use unrelated public servers as test targets.

---

## 🔐 Security

If you discover a security issue, do not immediately publish sensitive technical details publicly.

Provide the maintainer with enough information to understand and reproduce the issue while avoiding disclosure of:

- Credentials
- API keys
- Access tokens
- Private server information
- Personal information

---

## 📚 Documentation

Documentation contributions are encouraged.

Useful areas include:

- README
- Installation
- Configuration
- Troubleshooting
- Examples
- Architecture
- Compatibility notes
- Developer documentation

---

## 👥 Project Credits

### L1ghtXr

Original project creator and primary developer.

### DevBrezz

Project contributor.

Community contributors are credited through their respective contributions.

---

## 📜 License

By submitting a contribution to MCS, you agree that your contribution may be distributed under the project's MIT License.

# ai-native-sdlc

[![CI](https://github.com/skupriienko/ai-native-sdlc/actions/workflows/ci.yml/badge.svg)](https://github.com/skupriienko/ai-native-sdlc/actions)
[![Kilo Code Compatible](https://img.shields.io/badge/Kilo%20Code-Compatible-6366f1.svg)](https://kilo.org)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Types: Mypy](https://img.shields.io/badge/types-mypy-blue.svg)](https://mypy-lang.org/)

> **6-Phase Artifact Loop Engine & Spec-Driven Development Framework for AI Coding Agents**  
> Enforces Anthropic-style AI SDLC: intent.md -> spec.md -> plan.md -> tasks.md -> test-lock -> receipt.md.

---

## 🚀 Key Highlights

- **Pure Python Standard Library:** Zero heavy runtime dependencies. Lightning-fast startup (<10ms).
- **Native AI Tooling Integration:** Official first-class configuration for **Kilo Code**, **Claude Code**, **Cursor**, **Windsurf**, and **GitHub Copilot**.
- **Determinism & Performance:** Tested under extreme concurrency and heavy scale with sub-millisecond execution.
- **Enterprise-Grade Scaffolding:** Full modern PEP 517/621 packaging, PEP 561 typing (`py.typed`), Ruff linter, and pre-commit hooks.

---

## ⚡ Architecture & Workflow

```mermaid
flowchart LR
    A["Input / Task"] --> B["ai-native-sdlc Engine"]
    B --> C["Deterministic Verification"]
    C --> D["[RECEIPT] Clean Output"]
```

---

## 🤖 AI Tools Compatibility Matrix

| AI Environment | Integration Type | Path / Configuration |
| :--- | :--- | :--- |
| **Kilo / KiloCode** | Native Rules & Tools | `.kilo/kilo.jsonc` & `.kilo/rules/ai-native-sdlc.md` |
| **Cursor** | Project Rules | `.cursorrules` / `.kilo/rules/` |
| **Claude Code** | CLI & Sub-loops | Direct tool call via `sdlc` |
| **Windsurf** | Agent Rules | `.windsurfrules` |
| **Aider / Copilot** | CLI Utilities | Standard shell execution |

---

## 📦 Installation

```bash
# Clone and install in editable mode
git clone https://github.com/skupriienko/ai-native-sdlc.git
cd ai-native-sdlc
bash install.sh
```

Or install via `pip`:
```bash
pip install -e .
```

---

## 🛠️ CLI Usage

```bash
# Display help and available commands
sdlc --help
```

---

## 🧪 Testing & Stress Benchmarks

```bash
# Run pytest stress test suite
pytest -v tests/test_stress.py
```

---

## 📄 License

MIT © [Serhii Kupriienko](https://github.com/skupriienko)

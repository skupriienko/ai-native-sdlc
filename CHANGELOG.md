# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
with secondary CalVer release tracking (`YYYY.MM.DD.N`).

## [1.0.0] - 2026-11-02 (CalVer: 2026.11.02.1)

### Added
- Initial public open-source release of `ai-native-sdlc` (6-Phase Artifact Loop Engine & Spec-Driven Development).
- Enforces 6-phase artifact loop: intent.md -> spec.md -> plan.md -> tasks.md -> test-lock -> receipt.md.
- Spec-Driven Development gate checks preventing premature code mutation without validated design.
- Automated artifact scaffolding and completion status auditing.
- Native Kilo Code workflow rules and CLI commands.
- Full PEP 517/621 packaging (`pyproject.toml`, `setup.py`, `MANIFEST.in`, `src/*/py.typed`).
- Native Kilo Code / Kilo integration (`.kilo/kilo.jsonc`, `.kilo/rules/`, `.kilocoderules`).
- Developer tooling: Ruff linter, Mypy strict typing, pre-commit hooks, GitHub Actions CI matrix (Python 3.10–3.13).
- Comprehensive stress benchmarks under extreme concurrency (`tests/test_stress.py`).
- One-line deployment script (`install.sh`).
- Permissive MIT License.

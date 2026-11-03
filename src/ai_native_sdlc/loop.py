"""ai_native_sdlc — 6-Phase Artifact Loop Engine."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PHASES = ["intent", "spec", "plan", "tasks", "test_lock", "receipt"]

PHASE_TEMPLATES = {
    "intent": """# 1. PLAN: Intent & Outcome
- Problem: <What user friction or breakage occurred?>
- Proposed Outcome: <What observable result proves success?>
- Constraints: <Zero PII, zero server mutation, security invariants>
- Open Questions: <Ambiguities to resolve before spec>
""",
    "spec": """# 2. DESIGN: Specification
- Architecture: <Component boundaries and blast radius>
- Contracts: <Typed interfaces and schemas>
- Security: <OWASP, input sanitization, timeout defense>
""",
    "plan": """# 3. BUILD: Plan & Wave Breakdown
- Decisions: <Key architectural trade-offs>
- Execution Waves: <Disjoint parallel batches>
- Rollback Strategy: <One-command rollback procedure>
""",
    "tasks": """# 4. TASKS: Execution Register
- [ ] Task 1: Scaffolding and types
- [ ] Task 2: Core engine implementation
- [ ] Task 3: Stress and unit tests
""",
    "test_lock": """# 5. TEST: Test-Locking & Characterization
- Reproduction Test: <Locked failing test before fix>
- Concurrency & Stress: <Throughput limits>
- Pass Receipt: <Test suite output digest>
""",
    "receipt": """# 6. DEPLOY & RECEIPT: Attestation
- Status: SUCCESS
- Verification Hash: <sha256>
- Sensor Attestation: <all sensors pass>
""",
}


def sanitize_epic_name(epic_name: str) -> str:
    """Sanitizes epic name to prevent CWE-22 path traversal attacks."""
    clean = re.sub(r"[^a-zA-Z0-9_-]", "-", epic_name).strip("-")
    if not clean:
        raise ValueError("Invalid epic name: must contain alphanumeric characters")
    return clean


@dataclass(frozen=True)
class EpicReport:
    """Status report for a 6-phase artifact epic."""

    epic: str
    complete: bool
    phases: dict[str, bool]

    def to_dict(self) -> dict[str, Any]:
        return {
            "epic": self.epic,
            "complete": self.complete,
            "phases": self.phases,
        }


class SDLCManager:
    """Manages the 6-phase artifact loop for an epic with CWE-22 traversal protection."""

    def __init__(self, base_dir: Path | str = ".ai/artifacts") -> None:
        self.base_dir = Path(base_dir).resolve()

    def _resolve_epic_dir(self, epic_name: str) -> Path:
        safe_name = sanitize_epic_name(epic_name)
        target = (self.base_dir / safe_name).resolve()
        if not target.is_relative_to(self.base_dir):
            raise ValueError(
                f"Security Alert: Path traversal attempt blocked for epic '{epic_name}'"
            )
        return target

    def init_epic(self, epic_name: str) -> Path:
        """Creates the 6-phase markdown artifact files for the epic."""
        epic_dir = self._resolve_epic_dir(epic_name)
        epic_dir.mkdir(parents=True, exist_ok=True)
        for phase, template in PHASE_TEMPLATES.items():
            f = epic_dir / f"{phase}.md"
            if not f.exists():
                f.write_text(template, encoding="utf-8")
        return epic_dir

    def report(self, epic_name: str) -> EpicReport:
        """Returns typed EpicReport."""
        epic_dir = self._resolve_epic_dir(epic_name)
        status = {phase: (epic_dir / f"{phase}.md").exists() for phase in PHASES}
        return EpicReport(
            epic=sanitize_epic_name(epic_name),
            complete=all(status.values()),
            phases=status,
        )

    def check_epic(self, epic_name: str) -> dict[str, Any]:
        """Backward-compatible dictionary check."""
        return self.report(epic_name).to_dict()

    def list_epics(self) -> list[str]:
        """Lists all existing epics in base directory."""
        if not self.base_dir.exists():
            return []
        return sorted(
            [d.name for d in self.base_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]
        )

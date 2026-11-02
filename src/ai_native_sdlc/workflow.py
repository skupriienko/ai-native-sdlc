"""ai_native_sdlc — 6-Phase Artifact Loop Engine."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

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
"""
}

class SDLCManager:
    """Manages the 6-phase artifact loop for an epic."""

    def __init__(self, base_dir: Path | str = ".ai/artifacts") -> None:
        self.base_dir = Path(base_dir)

    def init_epic(self, epic_name: str) -> Path:
        epic_dir = self.base_dir / epic_name
        epic_dir.mkdir(parents=True, exist_ok=True)
        for phase, template in PHASE_TEMPLATES.items():
            f = epic_dir / f"{phase}.md"
            if not f.exists():
                f.write_text(template, encoding="utf-8")
        return epic_dir

    def check_epic(self, epic_name: str) -> Dict[str, Any]:
        epic_dir = self.base_dir / epic_name
        status = {}
        for phase in PHASES:
            f = epic_dir / f"{phase}.md"
            status[phase] = f.exists()
        return {
            "epic": epic_name,
            "complete": all(status.values()),
            "phases": status,
        }

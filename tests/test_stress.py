import time
from pathlib import Path

from ai_native_sdlc.loop import SDLCManager


def test_stress_sdlc_manager(tmp_path: Path):
    mgr = SDLCManager(tmp_path / "artifacts")

    # Init 100 epics concurrently
    t0 = time.perf_counter()
    for i in range(100):
        mgr.init_epic(f"epic_{i:03d}")
    duration = time.perf_counter() - t0

    assert duration < 0.5, f"100 epics initialized in {duration}s (expected <0.5s)"
    res = mgr.check_epic("epic_042")
    assert res["complete"] is True

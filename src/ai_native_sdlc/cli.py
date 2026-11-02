"""CLI interface for ai-native-sdlc."""
import argparse
import json
import sys
from pathlib import Path
from ai_native_sdlc.workflow import SDLCManager

def main() -> None:
    parser = argparse.ArgumentParser(
        description="sdlc: 6-Phase Artifact Loop Engine & Spec-Driven Development"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize artifacts for a new epic")
    init_parser.add_argument("epic", help="Epic or feature name")
    init_parser.add_argument("--dir", default=".ai/artifacts", help="Base directory")

    check_parser = subparsers.add_parser("check", help="Verify SDLC phase completion")
    check_parser.add_argument("epic", help="Epic name")
    check_parser.add_argument("--dir", default=".ai/artifacts", help="Base directory")

    args = parser.parse_args()
    mgr = SDLCManager(args.dir)

    if args.command == "init":
        p = mgr.init_epic(args.epic)
        print(f"\n🚀 Initialized 6-phase SDLC artifacts in: {p}")
        for phase in ["intent", "spec", "plan", "tasks", "test_lock", "receipt"]:
            print(f"  • {phase}.md")
    elif args.command == "check":
        res = mgr.check_epic(args.epic)
        print(json.dumps(res, indent=2))
        if not res["complete"]:
            sys.exit(1)

if __name__ == "__main__":
    main()

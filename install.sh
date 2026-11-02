#!/usr/bin/env bash
# One-liner installer for ai-native-sdlc
set -euo pipefail

echo "==> Installing ai-native-sdlc in editable mode..."
python3 -m pip install --upgrade pip
python3 -m pip install -e .

echo "==> Verifying installation of sdlc..."
sdlc --help >/dev/null

echo "==> Installation complete! Run 'sdlc --help' to get started."

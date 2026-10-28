#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist
rm -f dist/scout.skill
find scout -name '__pycache__' -type d -prune -exec rm -rf {} +
zip -qr dist/scout.skill scout -x '*.DS_Store' '*__pycache__*'
echo "built dist/scout.skill ($(du -h dist/scout.skill | cut -f1))"

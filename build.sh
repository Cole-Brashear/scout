#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist/chatgpt
find scout -name '__pycache__' -type d -prune -exec rm -rf {} +

# Claude Code, Cowork and Codex install the skill folder as a zip
rm -f dist/scout.skill
zip -qr dist/scout.skill scout -x '*.DS_Store' '*__pycache__*'

# ChatGPT gets the whole playbook as one project file, since a Project can't hold the folder structure
{
  echo "# Scout for ChatGPT"
  echo
  echo "This file bundles Scout's whole playbook. When it mentions a file such as \`references/onboarding.md\` or \`assets/profile-template.md\`, read the section below headed with that path. \`resume.py\` is a separate project file; \`jobs.py\` can't run in ChatGPT."
  for f in scout/SKILL.md scout/references/*.md scout/assets/*.md; do
    printf '\n\n---\n\n# FILE: %s\n\n' "${f#scout/}"
    cat "$f"
  done
} > dist/chatgpt/scout-chatgpt.md
cp scout/scripts/resume.py dist/chatgpt/resume.py

echo "built dist/scout.skill ($(du -h dist/scout.skill | cut -f1)) and dist/chatgpt/ ($(wc -w < dist/chatgpt/scout-chatgpt.md | tr -d ' ') words)"

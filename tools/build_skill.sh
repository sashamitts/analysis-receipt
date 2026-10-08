#!/usr/bin/env bash
# Copies the shared files into the Claude skill folder and packages it as a zip.
# Run from the repository root after editing anything in receipt/, guide/, prompts/, examples/ or tools/.
set -euo pipefail
S=skill/analysis-receipt
mkdir -p "$S/references" "$S/scripts"
cp receipt/analysis-receipt.md receipt/analysis-receipt-compact.md receipt/modules.md "$S/references/"
cp guide/ADAPTING.md guide/FILLING.md guide/LIMITS.md "$S/references/"
cp prompts/reader-briefs.md "$S/references/"
cp examples/learners-2026-demo.md "$S/references/example-learners-2026.md"
cp tools/leftover_sample.py "$S/scripts/"
rm -f skill/analysis-receipt.zip
(cd skill && zip -qr analysis-receipt.zip analysis-receipt -x '*.DS_Store')
echo "Built skill/analysis-receipt.zip"

#!/usr/bin/env bash
# Thin wrapper around render-audit-pdf.py so callers can use a stable .sh path.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/render-audit-pdf.py" "$@"

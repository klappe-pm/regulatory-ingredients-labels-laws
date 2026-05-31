#!/usr/bin/env bash
set -euo pipefail

installer="/Users/kevinlappe/.claude/scripts/scaffold-new-project.sh"
if [ ! -x "$installer" ]; then
  scaffold_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  installer="$(cd "$scaffold_dir/../.." && pwd)/scripts/scaffold-new-project.sh"
fi

exec "$installer" "$@"

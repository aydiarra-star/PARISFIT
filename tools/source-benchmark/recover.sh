#!/usr/bin/env bash
# Public artifacts only. No credentials are requested or embedded.
set -euo pipefail
run="${1:?Usage: bash tools/source-benchmark/recover.sh RUN_ID}"
[[ "$run" =~ ^[0-9]+$ ]] || { echo 'Numeric run ID required' >&2; exit 2; }
dest=".cache/phase12-download-$run"
gh run download "$run" --repo aydiarra-star/PARISFIT --name phase12-source-benchmark --dir "$dest"
echo "Extracted to $dest. Open index.html. If expired, rerun the pinned workflow; do not silently substitute a new dataset."

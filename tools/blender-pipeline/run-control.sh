#!/bin/sh
# Public fixture only. Run from repository root. No personal uploads or activation.
set -eu
mkdir -p .cache/phase9
blender --background --factory-startup --python-exit-code 1 --python tools/blender-pipeline/retarget.py > .cache/phase9/blender.log 2>&1
# Serve repo on port 3000 separately; never start an unmanaged server here.
node tools/blender-pipeline/check.cjs

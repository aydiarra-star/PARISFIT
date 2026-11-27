#!/bin/sh
# Run only on an authorized Ubuntu 24.04 machine. Does not install in Arena.
set -eu
sudo apt-get update
sudo apt-get install -y blender python3-numpy python3-requests libxrender1 libxxf86vm1 libxfixes3 libxi6 libxkbcommon0 libsm6 libice6 libgl1 libegl1 libx11-6 libxext6 libgomp1
blender --version

#!/bin/sh
# Isolated Python 3.11 environment recommended. No paid service or upload.
set -eu
PYTHON="${PYTHON:-.venv/bin/python}"
"$PYTHON" -m pip install 'mediapipe==0.10.21' 'imageio-ffmpeg==0.6.0' 'Pillow==12.0.0'
# MediaPipe's wheel declares the GUI OpenCV package; use equivalent headless bindings in this sandbox.
"$PYTHON" -m pip uninstall -y opencv-contrib-python
"$PYTHON" -m pip install 'opencv-contrib-python-headless==4.11.0.86'

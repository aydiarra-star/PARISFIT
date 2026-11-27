# Prepared, NOT built in Arena. Pin image digest + apt snapshot before qualification.
FROM python:3.11-slim-bookworm
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxrender1 libxxf86vm1 libxfixes3 libxi6 libxkbcommon0 libsm6 libice6 libgl1 \
    libx11-6 libxext6 libegl1 libgomp1 \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir bpy==4.2.0 numpy==1.26.4
WORKDIR /work
ENV OMP_NUM_THREADS=2
# No display required, but X/GL shared libraries must still resolve.
RUN python -c "import bpy; assert bpy.app.version_string.startswith('4.2'); print(bpy.app.version_string)"
ENTRYPOINT ["python", "tools/capture-pipeline/blender-smoke.py"]

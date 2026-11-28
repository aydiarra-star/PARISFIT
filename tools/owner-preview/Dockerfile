# Build with repository root as context. Runtime contains only the demo allowlist.
FROM python:3.12-slim AS builder
WORKDIR /source
COPY . .
RUN python3 tools/owner-preview/build_demo.py
FROM python:3.12-slim
WORKDIR /srv
COPY --from=builder /source/.cache/owner-demo /srv/.cache/owner-demo
COPY tools/owner-preview/demo_server.py /srv/tools/owner-preview/demo_server.py
ENV PORT=8080 COOKIE_SECURE=1
EXPOSE 8080
USER 65534:65534
CMD ["sh", "-c", "test -n \"$PARISFIT_DEMO_PASSWORD\" && exec python3 tools/owner-preview/demo_server.py"]

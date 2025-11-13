#!/bin/bash
set -e

# Default uvicorn command with production settings
exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 4 \
    --backlog 4096 \
    --limit-concurrency 2000 \
    --timeout-keep-alive 30 \
    --timeout-graceful-shutdown 30 \
    "$@"

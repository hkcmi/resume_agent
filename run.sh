#!/usr/bin/env bash
set -euo pipefail

if [[ -f ".env" ]]; then
  set -a
  source .env
  set +a
fi

if [[ -z "${DEEPSEEK_API_KEY:-}" ]]; then
  echo "DEEPSEEK_API_KEY is required. Put it in .env or export it before running."
  exit 1
fi

export PYTHONPATH="${PYTHONPATH:-/app}"
streamlit run app/streamlit_app.py --server.address=0.0.0.0 --server.port="${PORT:-8501}"

#!/bin/bash
# Check if virtual env exists
if [ ! -d "agent_venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv agent_venv
fi

source agent_venv/bin/activate

# Check if GITLAB_TOKEN is set
if [ -z "$GITLAB_TOKEN" ]; then
    echo "Warning: GITLAB_TOKEN is not set. Auto-response actions will be disabled."
fi

echo "Starting SentinelOps Agent on http://localhost:8000"
echo "GitLab Webhook URL: http://<your-public-ip-or-domain>:8000/webhook"
echo "Incident Dashboard: http://localhost:8000/"

export GOOGLE_APPLICATION_CREDENTIALS="sentinelops-agent-key.json"
uvicorn sentinel_ops.main:app --host 0.0.0.0 --port 8000 --reload

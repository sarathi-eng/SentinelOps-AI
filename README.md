# SentinelOps AI — Autonomous Incident Commander

SentinelOps AI is an autonomous, AI-powered incident response platform built for modern DevOps teams. It monitors GitLab events and uses Gemini on Google Cloud Vertex AI to autonomously investigate failures, identify root causes, and recommend remediation actions.

## 🚀 Features
- **Autonomous Incident Detection:** Listens to GitLab CI/CD webhooks.
- **Gemini-Powered Root Cause Analysis:** Expert-level reasoning on logs and commits.
- **Executive Dashboards:** High-density UI with business metrics (MTTR, Downtime Prevented).
- **Automated Actions:** GitLab issue creation and rollback recommendations.
- **Cinematic Storytelling:** Detailed incident timelines and AI confidence scores.

## 🛠 Tech Stack
- **AI:** Google Cloud Vertex AI (Gemini 1.5 Flash)
- **Backend:** FastAPI, Python
- **Frontend:** Vanilla CSS/HTML
- **Infrastructure:** Cloud Run, BigQuery (Roadmap)
- **Integrations:** GitLab API

## 🚦 Quick Start

### 1. Prerequisites
- Google Cloud Project with Billing Enabled.
- GitLab Personal Access Token.
- Python 3.12+.

### 2. Setup
```bash
# Clone the repository
git clone <repo-url>
cd sentinel-ops

# Create and activate virtual environment
python3 -m venv agent_venv
source agent_venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
1. Create a service account in GCP with `Vertex AI User` permissions.
2. Download the JSON key as `sentinelops-agent-key.json` and place it in the root.
3. Set your GitLab token:
```bash
export GITLAB_TOKEN=your_token_here
```

### 4. Running the Platform
```bash
./run_sentinel.sh
```
The dashboard will be available at `http://localhost:8000/`.

## 🏆 Demo Mode
To see the system in action without a live GitLab failure:
```bash
python3 simulate_incident.py
```

## 📄 License
MIT License - See [LICENSE](LICENSE) for details.

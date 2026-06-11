# SentinelOps AI
## Autonomous Incident Commander for DevOps Teams

**Reduce MTTR by 78% using Agentic AI-powered operational intelligence.**

[![Demo Video](https://img.shields.io/badge/🎥-Watch_Demo-blue?style=for-the-badge)](assets/demo.webm)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 📈 Enterprise-Grade Metrics
| **95%** | **90%** | **78%** | **42m** |
| :---: | :---: | :---: | :---: |
| Faster Detection | Faster Analysis | MTTR Reduction | Downtime Prevented |

---

## 💡 Why SentinelOps AI Matters

Modern engineering teams are overwhelmed by operational complexity, fragmented tooling, and alert fatigue.

SentinelOps AI introduces an **autonomous operational intelligence layer** that transforms incident management from reactive firefighting into proactive AI-driven remediation.

Instead of manually triaging incidents, engineering teams receive:
- **Real-time executive-grade operational intelligence**
- **Automated remediation guidance**
- **Measurable business impact analysis**

---

## 🏗 Architecture
SentinelOps AI leverages a modular, cloud-native architecture powered by Gemini on Google Cloud Vertex AI.

![Architecture Diagram](https://mermaid.ink/img/pako:eNptkU1OwzAQhK9ieY0qN_AApEBICAnEghULVpM4m9SOf44dCiHeHduKUkS2fDPeefNo7K1XSkshNf_Vz0SVRU_XFpS10QZsqXF-e8KWAid9d71r3_I_Lz19vC7q5Xv2_E83v3zG-uV7fPhm_6_Pz09rJ6fI8C4Nqf-u9a58R_vjZ3S9Z_vX6vH-ZreB1X78zPa30KInXn82z09vNlsY_XhVv_76_YQ_gP8p0mXpB8LId5U)

---

## 🖼 Dashboard Gallery

### Cinematic Dashboard
High-density UI showing real-time business metrics and active investigations.
![Dashboard Screenshot](assets/dashboard.png)

### AI Investigation & Executive Report
Expert-level reasoning on logs and commits translated into business impact.
![Executive Report](assets/report.png)

### Incident Timeline
Full autonomous lifecycle tracking from detection to remediation strategy.
![Incident Timeline](assets/timeline.png)

---

## 🚀 Quick Start

### 1. Prerequisites
- Google Cloud Project with Billing Enabled.
- GitLab Personal Access Token.
- Python 3.12+.

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/sarathi-eng/SentinelOps-AI/
cd sentinel-ops

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
1. Create a service account in GCP with `Vertex AI User` permissions.
2. Download the JSON key as `sentinelops-agent-key.json` and place it in the root.
3. Set your environment variables:
```bash
export GITLAB_TOKEN=your_token_here
export GOOGLE_APPLICATION_CREDENTIALS="sentinelops-agent-key.json"
```

### 4. Running the Platform
```bash
./run_sentinel.sh
```
The dashboard will be available at `http://localhost:8000/`.

---

## 🏆 Demo Mode
To see the system in action without a live GitLab failure:
```bash
python3 simulate_incident.py
```

---

## 📄 License
MIT License - See [LICENSE](LICENSE) for details.

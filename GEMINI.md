# Project Alpha: Core Stack & Conventions

## Core Stack
- **AI / Agent Layer:**
  - **Gemini API / Vertex AI:** Used for reasoning and agent orchestration.
  - **Agent Builder:** Used for advanced reasoning workflows.
- **Hosting / Backend:**
  - **Cloud Run:** For hosting the backend API. (Requires Billing)
  - **Firebase:** For frontend hosting and Auth.
- **Monitoring / Storage:**
  - **BigQuery:** For analytics and log storage.
  - **Cloud Logging:** For system monitoring.

## Infrastructure
- **Service Account:** `sentinelops-agent@alfolite.iam.gserviceaccount.com`
- **Authentication:** Use `sentinelops-agent-key.json` for local development and backend service authentication. **DO NOT COMMIT THIS KEY.**
- **Project ID:** `alfolite`

## Development Workflow
- **Demo-First Strategy:** All changes must prioritize visual impact and operational storytelling.
- **AI Output:** Use the "Executive-Friendly" schema (Root Cause, Impact, Recommendation, Confidence, Timeline).
- **Dashboard:** Maintain high-density, professional UI using Vanilla CSS. Use the `sentinel_ops/dashboard/` assets.
- **Simulation:** Use `simulate_incident.py` for testing and live demos.

## Security
- Secrets should be stored in environment variables.
- Add `*-key.json`, `.env`, and `incidents.json` to `.gitignore`.

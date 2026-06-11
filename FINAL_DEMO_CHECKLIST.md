# SentinelOps AI: Final Demo Checklist

## 🛠 Preparation
- [ ] Ensure `sentinelops-agent-key.json` is in the root directory.
- [ ] Export GitLab Token: `export GITLAB_TOKEN=your_token_here`.
- [ ] Verify Virtual Environment: `source agent_venv/bin/activate`.

## 🚀 Execution Flow
- [ ] **Step 1:** Start Backend Server: `./run_sentinel.sh`.
- [ ] **Step 2:** Launch Dashboard: Open `http://localhost:8000/`.
- [ ] **Step 3:** Trigger Simulation: Run `python simulate_incident.py`.
- [ ] **Step 4:** Observe Dashboard:
    - [ ] Pulse investigation active.
    - [ ] Metric count-up animations.
    - [ ] Timeline rendering.
    - [ ] Executive report visibility.

## 📦 Submission Assets
- [ ] Record Demo Video (use `DEMO_SCRIPT.md`).
- [ ] Capture High-Res Screenshots.
- [ ] Verify `SUBMISSION.md` on Devpost.
- [ ] Push Code to Public Repository.
- [ ] Verify `LICENSE` and `README.md`.

## ✅ Final Verification
- [ ] Dashboard is responsive on mobile/desktop.
- [ ] No console errors in browser.
- [ ] No log errors in backend.
- [ ] System handles multiple incidents gracefully.

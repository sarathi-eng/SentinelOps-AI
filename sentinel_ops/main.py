from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .analyzer import analyze_incident
from .actions import handle_auto_response
import json
import os

app = FastAPI(title="SentinelOps GitLab Listener")

# Serve the static dashboard
@app.get("/")
async def serve_dashboard():
    return FileResponse("sentinel_ops/dashboard/index.html")

@app.post("/webhook")
async def gitlab_webhook(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    event_type = request.headers.get("X-Gitlab-Event")
    
    print(f"Received GitLab event: {event_type}")
    
    # We are interested in Pipeline Hooks and Merge Request Hooks
    if event_type == "Pipeline Hook":
        status = payload.get("object_attributes", {}).get("status")
        if status == "failed":
            print("Detected failed pipeline. Triggering analysis...")
            background_tasks.add_task(process_pipeline_failure, payload)
            
    return {"status": "accepted"}

async def process_pipeline_failure(payload: json):
    # Module 2: Analyze Incident
    analysis = await analyze_incident(payload)
    
    # Module 4: Auto Response Actions
    if analysis:
        await handle_auto_response(payload, analysis)

@app.get("/incidents")
async def get_incidents():
    # Placeholder for Module 3 (Dashboard) to fetch data
    try:
        with open("incidents.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

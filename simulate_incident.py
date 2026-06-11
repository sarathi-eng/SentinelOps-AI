import requests
import json
import time

URL = "http://localhost:8000/webhook"

def simulate_pipeline_failure():
    payload = {
        "object_kind": "pipeline",
        "object_attributes": {
            "id": 12345,
            "status": "failed",
            "ref": "main"
        },
        "project": {
            "id": 99,
            "name": "SentinelOps-Webapp"
        }
    }
    
    headers = {
        "X-Gitlab-Event": "Pipeline Hook",
        "Content-Type": "application/json"
    }
    
    print(f"Triggering simulated pipeline failure event for project: {payload['project']['name']}")
    try:
        response = requests.post(URL, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}. Is the SentinelOps server running?")

if __name__ == "__main__":
    simulate_pipeline_failure()

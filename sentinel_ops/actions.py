import os
import gitlab

async def handle_auto_response(payload: dict, analysis: dict):
    token = os.getenv("GITLAB_TOKEN")
    if not token:
        print("Warning: GITLAB_TOKEN not set. Skipping auto-response actions.")
        return

    project_id = payload.get("project", {}).get("id")
    gl = gitlab.Gitlab("https://gitlab.com", private_token=token)
    
    try:
        project = gl.projects.get(project_id)
        
        # Create an issue with the AI analysis
        title = f"AI Incident Report: Pipeline #{analysis['pipeline_id']} Failed"
        description = f"""
## Incident Analysis by SentinelOps (Gemini)
**Severity:** {analysis['severity']}
**Root Cause:** {analysis['root_cause']}

### Recommendation
{analysis['recommendation']}

---
*Generated automatically by SentinelOps Agent.*
"""
        project.issues.create({'title': title, 'description': description})
        print(f"Successfully created GitLab issue for pipeline #{analysis['pipeline_id']}")
        
    except Exception as e:
        print(f"Error executing GitLab actions: {e}")

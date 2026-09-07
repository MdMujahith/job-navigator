# tools/interview_tools.py
from langchain_core.tools import tool
from typing import Optional
import requests

base_url = "http://127.0.0.1:8000"

@tool
def list_interviews() -> str:
    """List all interviews."""
    try:
        response = requests.get(f"{base_url}/interviews")
        response.raise_for_status()
        return str(response.json())
    except Exception as e:
        return f"Error listing interviews: {str(e)}"

@tool
def create_interview(job_id: int, title: str, status: str, stage: str,
                      interview_schedule: str, note: Optional[str] = None) -> str:
    """Create a new interview linked to a job. job_id must reference an existing job — check with list_jobs first if unsure. interview_schedule should be an ISO datetime string, e.g. '2026-09-15T14:00:00'."""
    try:
        payload = {
            "job_id": job_id, "title": title, "status": status, "stage": stage,
            "interview_schedule": interview_schedule, "note": note,
        }
        response = requests.post(f"{base_url}/add_interview", json=payload)
        response.raise_for_status()
        return f"Interview created: {response.json()}"
    except Exception as e:
        return f"Error creating interview: {str(e)}"

@tool
def update_interview(interview_id: int, title: Optional[str] = None, status: Optional[str] = None,
                      stage: Optional[str] = None, interview_schedule: Optional[str] = None,
                      note: Optional[str] = None) -> str:
    """Update an existing interview by ID. Only include the fields you want to change."""
    try:
        payload = {k: v for k, v in {
            "title": title, "status": status, "stage": stage,
            "interview_schedule": interview_schedule, "note": note
        }.items() if v is not None}
        response = requests.patch(f"{base_url}/update_interview/{interview_id}", json=payload)
        response.raise_for_status()
        return f"Interview updated: {response.json()}"
    except Exception as e:
        return f"Error updating interview: {str(e)}"

@tool
def delete_interview(interview_id: int) -> str:
    """Delete an interview by ID."""
    try:
        response = requests.delete(f"{base_url}/delete_interview/{interview_id}")
        response.raise_for_status()
        return f"Interview {interview_id} deleted successfully."
    except Exception as e:
        return f"Error deleting interview: {str(e)}"
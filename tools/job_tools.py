# tools/job_tools.py
from langchain_core.tools import tool
from typing import Optional
import requests

base_url = "http://127.0.0.1:8000"

@tool
def list_jobs() -> str:
    """List all job postings."""
    try:
        response = requests.get(f"{base_url}/jobs")
        response.raise_for_status()
        return str(response.json())
    except Exception as e:
        return f"Error listing jobs: {str(e)}"

@tool
def create_job(company_id: int, title: str, description: str, posted_date: str, salary: float, apply_link: str) -> str:
    """Create a new job posting. posted_date must be a string in YYYY-MM-DD format. company_id must reference an existing company — check with list_companies first if unsure."""
    try:
        payload = {
            "company_id": company_id,
            "title": title,
            "description": description,
            "posted_date": posted_date,
            "salary": salary,
            "apply_link": apply_link,
        }
        response = requests.post(f"{base_url}/add_job", json=payload)
        response.raise_for_status()
        return f"Job created: {response.json()}"
    except Exception as e:
        return f"Error creating job: {str(e)}"

@tool
def update_job(job_id: int, title: Optional[str] = None, description: Optional[str] = None,
                posted_date: Optional[str] = None, salary: Optional[float] = None,
                apply_link: Optional[str] = None) -> str:
    """Update an existing job posting by ID. Only include the fields you want to change."""
    try:
        payload = {k: v for k, v in {
            "title": title, "description": description, "posted_date": posted_date,
            "salary": salary, "apply_link": apply_link
        }.items() if v is not None}
        response = requests.patch(f"{base_url}/update_job/{job_id}", json=payload)
        response.raise_for_status()
        return f"Job updated: {response.json()}"
    except Exception as e:
        return f"Error updating job: {str(e)}"

@tool
def delete_job(job_id: int) -> str:
    """Delete a job posting by ID."""
    try:
        response = requests.delete(f"{base_url}/delete_job/{job_id}")
        response.raise_for_status()
        return f"Job {job_id} deleted successfully."
    except Exception as e:
        return f"Error deleting job: {str(e)}"
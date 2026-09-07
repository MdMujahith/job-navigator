# tools/company_tools.py
from langchain_core.tools import tool
from typing import Optional
import requests

base_url = "http://127.0.0.1:8000"

@tool
def list_companies() -> str:
    """List all companies, including their IDs. Use this before creating a job if you don't know a valid company_id."""
    try:
        response = requests.get(f"{base_url}/companies")
        response.raise_for_status()
        return str(response.json())
    except Exception as e:
        return f"Error listing companies: {str(e)}"

@tool
def create_company(name: str, website: Optional[str] = None, location: Optional[str] = None,
                    industry: Optional[str] = None) -> str:
    """Create a new company record."""
    try:
        payload = {"name": name, "website": website, "location": location, "industry": industry}
        response = requests.post(f"{base_url}/add_company", json=payload)
        response.raise_for_status()
        return f"Company created: {response.json()}"
    except Exception as e:
        return f"Error creating company: {str(e)}"

@tool
def update_company(company_id: int, name: Optional[str] = None, website: Optional[str] = None,
                    location: Optional[str] = None, industry: Optional[str] = None) -> str:
    """Update an existing company by ID. Only include the fields you want to change."""
    try:
        payload = {k: v for k, v in {
            "name": name, "website": website, "location": location, "industry": industry
        }.items() if v is not None}
        response = requests.patch(f"{base_url}/update_company/{company_id}", json=payload)
        response.raise_for_status()
        return f"Company updated: {response.json()}"
    except Exception as e:
        return f"Error updating company: {str(e)}"

@tool
def delete_company(company_id: int) -> str:
    """Delete a company by ID."""
    try:
        response = requests.delete(f"{base_url}/delete_company/{company_id}")
        response.raise_for_status()
        return f"Company {company_id} deleted successfully."
    except Exception as e:
        return f"Error deleting company: {str(e)}"
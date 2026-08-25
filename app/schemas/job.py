from pydantic import BaseModel
from datetime import date

class JobCreate(BaseModel):
    company_id:int
    title:str
    description:str
    posted_date:date
    salary:float
    apply_link:str

class JobOut(BaseModel):
    id:int
    company_id:int
    title:str
    description:str
    posted_date:date
    salary:float
    apply_link:str

class JobUpdate(BaseModel):
    company_id:int | None = None
    title:str | None = None
    description:str | None = None
    posted_date:date | None = None
    salary:float | None = None
    apply_link:str | None = None
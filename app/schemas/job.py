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

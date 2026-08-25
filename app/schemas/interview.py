from pydantic import BaseModel
from datetime import date

class InterviewCreate(BaseModel):
    job_id:int
    title:str
    status:str
    stage:str
    interview_schedule:date
    note:str

class InterviewOut(BaseModel):
    id:int
    job_id:int
    title:str
    status:str
    stage:str
    interview_schedule:date
    note:str

class InterviewUpdate(BaseModel):
    job_id:int | None = None
    title:str | None = None
    status:str | None = None
    stage:str | None = None
    interview_schedule:date | None = None
    note:str | None = None
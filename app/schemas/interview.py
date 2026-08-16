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
#main.py
from fastapi import FastAPI 
from app.database import SessionLocal,engine,Base
from app.models.company import Company
from app.models.job import Job
from app.models.interview import Interview
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def status():
    return {"status":"healthy"}

@app.get("/jobs")
def get_all_jobs():
    pass
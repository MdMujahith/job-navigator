#main.py
from fastapi import FastAPI, Depends, HTTPException
from app.database import SessionLocal,engine,Base,get_db
from datetime import date

#DataBase Models of  getting Meta Data
from app.models.company import Company
from app.models.job import Job
from app.models.interview import Interview

#Pydantic Models to Use as template for OutPut Data
from app.schemas.job import JobCreate,JobOut,JobUpdate
from app.schemas.interview import InterviewCreate,InterviewOut,InterviewUpdate
from app.schemas.company import CompanyCreate,CompanyOut,CompanyUpdate
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()
 
@app.get("/")
def status():
    return {"status":"healthy"}

#Job Routes

#Getting All Jobs
@app.get("/jobs",response_model=list[JobOut])
def get_all_jobs(db:Session = Depends(get_db)):
    return db.query(Job).all()

#Adding New Job
@app.post("/add_job",response_model=JobOut)
def add_job_to_db(job:JobCreate, db:Session = Depends(get_db)):
    new_job = Job(
            company_id =job.company_id,
            title = job.title,
            description = job.description,
            posted_date = job.posted_date,
            salary = job.salary,
            apply_link = job.apply_link)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

#Updating Job
@app.patch("/update_job/{id}",response_model=JobOut)
def update_job_to_db(id:int,job:JobUpdate,db:Session = Depends(get_db)):
    update_job=db.query(Job).filter(Job.id == id).first()
    if update_job:
            for key,values in job.model_dump(exclude_none=True).items():
                setattr(update_job,key,values)
            db.commit()
            db.refresh(update_job)
            return update_job
    else:
         raise HTTPException(status_code=404, detail="Job not found")
#Deleting Job  
@app.delete("/delete_job/{id}",status_code=204)
def delete_job_to_db(id:int,db:Session = Depends(get_db)):
    delete_job=db.query(Job).filter(Job.id == id).first()
    if delete_job:
      db.delete(delete_job)
      db.commit()
      return
    else:
        raise HTTPException(status_code=404, detail="Job not found") 


#Company Routes
#Getting All Companies
@app.get("/companies",response_model=list[CompanyOut])
def get_all_companies(db:Session = Depends(get_db)):
    return db.query(Company).all()

#Adding Companies
@app.post("/add_company",response_model=CompanyOut)
def add_company_to_db(company:CompanyCreate, db:Session = Depends(get_db)):
    new_company = Company(
                name=company.name,
                website=company.website,
                location=company.location,
                industry=company.industry)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

#Updating Companies
@app.patch("/update_company/{id}",response_model=CompanyOut)
def update_company_to_db(id:int,company:CompanyUpdate,db:Session = Depends(get_db)):
    update_company=db.query(Company).filter(Company.id == id).first()
    if update_company:
            for key,values in company.model_dump(exclude_none=True).items():
                setattr(update_company,key,values)
            db.commit()
            db.refresh(update_company)
            return update_company
    else:
         raise HTTPException(status_code=404, detail="Company not found")
    
#Deleting Companies  
@app.delete("/delete_company/{id}",status_code=204)
def delete_company_to_db(id:int,db:Session = Depends(get_db)):
    delete_company=db.query(Company).filter(Company.id == id).first()
    if delete_company:
      db.delete(delete_company)
      db.commit()
      return
    else:
        raise HTTPException(status_code=404, detail="Company not found")

#Interview Routes
@app.get("/interviews",response_model=list[InterviewOut])
def get_all_interviews(db:Session = Depends(get_db)):
    return db.query(Interview).all()

#Adding New Interview
@app.post("/add_interview",response_model=InterviewOut)
def add_interview_to_db(interview:InterviewCreate, db:Session = Depends(get_db)):
    new_interview = Interview(
            job_id = interview.job_id,
            title = interview.title,
            status = interview.status,
            stage = interview.stage,
            interview_schedule = interview.interview_schedule,
            note=interview.note)
    db.add(new_interview)
    db.commit()
    db.refresh(new_interview)
    return new_interview

#Updating Interview
@app.patch("/update_interview/{id}",response_model=InterviewOut)
def update_interview_to_db(id:int,interview:InterviewUpdate,db:Session = Depends(get_db)):
    update_interview=db.query(Interview).filter(Interview.id == id).first()
    if update_interview:
            for key,values in interview.model_dump(exclude_none=True).items():
                setattr(update_interview,key,values)
            db.commit()
            db.refresh(update_interview)
            return update_interview
    else:
         raise HTTPException(status_code=404, detail="Interview not found")
    
#Deleting Interview  
@app.delete("/delete_interview/{id}",status_code=204)
def delete_interview_to_db(id:int,db:Session = Depends(get_db)):
    delete_interview=db.query(Interview).filter(Interview.id == id).first()
    if delete_interview:
      db.delete(delete_interview)
      db.commit()
      return
    else:
        raise HTTPException(status_code=404, detail="Interview not found")
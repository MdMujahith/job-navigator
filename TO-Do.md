#Interview Routes
@app.get("/interviews",response_model=list[InterviewOut])
def get_all_interviews(db:Session = Depends(get_db)):
    return db.query(Interview).all()

#Adding New Interview
@app.post("/add_interview",response_model=InterviewOut)
def add_interview_to_db(interview:InterviewCreate, db:Session = Depends(get_db)):
    new_interview = Interview(
            company_id =interview.company_id,
            title = interview.title,
            description = interview.description,
            posted_date = interview.posted_date,
            salary = interview.salary,
            apply_link = interview.apply_link)
    db.add(new_interview)
    db.commit()
    db.refresh(new_interview)
    return new_interview

#Updating Interview
@app.patch("/update_interview/{id}/{field}",response_model=InterviewUpdate)
def update_interview_to_db(id:int, field:str,interview:InterviewUpdate,db:Session = Depends(get_db)):
    update_interview=db.query(Interview).filter(Interview.id == id).first()
    if update_interview:
            setattr(update_interview,field,getattr(interview,field))
            db.commit()
            db.refresh(update_interview)
            return update_interview
    else:
         return "No Interview Found"
#Deleting Interview  
@app.delete("/delete_interview/{id}")
def delete_interview_to_db(id:int,db:Session = Depends(get_db)):
    delete_interview=db.query(Interview).filter(Interview.id == id).first()
    if delete_interview:
      db.delete(delete_interview)
      db.commit()
      return
    else:
        return "Value not Found" 
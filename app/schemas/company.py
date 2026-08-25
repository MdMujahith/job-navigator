from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name:str
    website:str
    location:str
    industry:str

class CompanyOut(BaseModel):
    id:int
    name:str
    website:str
    location:str
    industry:str

class CompanyUpdate(BaseModel):
    name:str | None = None
    website:str | None = None
    location:str | None = None
    industry:str | None = None
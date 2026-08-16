from pydantic import BaseModel

class Company(BaseModel):
    id:int
    name:str
    website:str
    location:str
    industry:str
from pydantic import BaseModel
from typing import Optional

class demo(BaseModel):
    name:str
    profession:str
    mobileNumber:str
    email:str
    weddingStatus:str
    month:str
    budget:str
    country:str
    city:str
    message:str
    isDeleted:bool=False


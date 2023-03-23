from pydantic import BaseModel
from typing import Optional

class training(BaseModel):
    name:str
    email:str
    mobileNumber:str
    profession:str
    city:str
    isDeleted:bool=False


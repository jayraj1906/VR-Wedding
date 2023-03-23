from pydantic import BaseModel
from typing import Optional

class refferal(BaseModel):
    mobileNumber:str
    profession:str=None
    name:str=None
    city:str=None
    isDeleted:bool=False

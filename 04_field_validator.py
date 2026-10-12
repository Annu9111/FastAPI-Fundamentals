from pydantic import BaseModel,EmailStr,Field,AnyUrl
from typing import List ,Dict,Optional,Annotated

class Patients(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact:Dict[str,str]
    
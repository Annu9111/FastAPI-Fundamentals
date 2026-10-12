from pydantic import BaseModel,model_validator,EmailStr
from typing import List ,Dict,Optional,Annotated

class Patients(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact:Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age >60 and'emergency' not in model.contact:
            raise ValueError('patient older than 60')

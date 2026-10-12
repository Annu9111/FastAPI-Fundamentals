from pydantic import BaseModel,EmailStr,Field,AnyUrl,field_validator
from typing import List ,Dict,Optional,Annotated

class Patients(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact:Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_doman=["hdfc.com","icici.com"]
        domain_name=value.split('@')[-1]
        
        if domain_name not in valid_doman:
            raise ValueError('not a valid doman')
        
        return value


    @field_validator('name')
    @classmethod
    def name_validator(cls,value):
        return value.upper()
    
        
    
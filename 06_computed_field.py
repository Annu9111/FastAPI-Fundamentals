from pydantic import BaseModel,computed_field,EmailStr
from typing import List ,Dict,Optional,Annotated

class Patients(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact:Dict[str,str]
    
    
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height)**2,2)
        return bmi
            
    
from pydantic import BaseModel,EmailStr,Field,AnyUrl
from typing import List ,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='name of the patient')]
    Email :EmailStr
    linkden:AnyUrl
    age:int
    weight:float = Field(gt=0)
    married:bool
    allergies:Optional[List[str]] =None
    contact_detail :Dict[str,str]
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.Email)
        
    
patient_info ={'name':'riya','Email':'anu@sd.com','linkden':'hhtps/lindiv/123','age':40,'weight':34.5,'married':False,'allergies':['polen', 'dust'],'contact_detail':{'email':'anu@123','phone':234}}

p1=Patient(**patient_info )    

insert_patient_data(p1)

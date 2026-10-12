from pydantic import BaseModel
from typing import List ,Dict

class Patient(BaseModel):
    name:str
    age:int
    weight:int
    married:bool
    allergies:List[str]
    contact_detail :Dict[str,str]
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
        
    
patient_info ={'name':'riya','age':40,'weight':34.5,'married':False,'allergies':['polen', 'dust'],'contact_detail':{'email':'anu@123','phone':234}}

p1=Patient(**patient_info )    

insert_patient_data(p1)

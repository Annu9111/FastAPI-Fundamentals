from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
        
    
patient_info ={'name':'riya','age':40}
p1=Patient(**patient_info )    

insert_patient_data(p1)

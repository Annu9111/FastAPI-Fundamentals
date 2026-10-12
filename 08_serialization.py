from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str
    

class Patient(BaseModel):
    name:str
    gender:str
    age:int 
    address:Address

add_dic={'city':'haryana','state':'tuna','pin':'1234'}

add1=Address(**add_dic)

Patient_dic={'name':'riya','gender':'female','age':23,'address':add1}

Patient1=Patient(**Patient_dic)

print(Patient1)

Patient1.model_dump(include=['name','gender'])

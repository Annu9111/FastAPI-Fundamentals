from pydantic import BaseModel,Field,computed_field
from fastapi import FastAPI,Path,HTTPException,Query
from typing import Annotated,Literal
import json


app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description='ID of the patients',examples='like P001,P002 and so on')]
    
    name:Annotated[str,Field(...,description='name of the patient')]
    
    city:Annotated[str,Field(...,discription="city of the patient")]
    
    age:Annotated[int,Field(...,discription="age of the patient")]
    
    gender:Annotated[Literal['male','female','other'],Field(...,discription='gender of the patient')]
    
    height:Annotated[float,Field(...,gt=0,discription="height of the patient in meters")]
    
    weight:Annotated[float,Field(...,gt=0,discription="weight of the patient in kg")]
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height)**2,2)
        return bmi 
    
    


def load_data():
    with open("02_patients.json","r") as f :
        data = json.load(f)
    return data    
    

@app.get('/')
def greet():
    return {'message':'Patients Management System Api'}

@app.get('/about')
def about():
    return {'message':'A fully functional api to manage patients record'}

@app.get('/view')
def view():
    data = load_data()
    return data
    
@app.get('/patient/{patient_id}')
def patient(patient_id : str=Path(...,description="Id required")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="patient not found")  
    
@app.get('/sort')
def sort_patient(sort_by:str = Query(...,description="sort on the basis of height,weight or bmi"),order:str=Query('asc',description="sort in ascending and decending order")):
    vaild_feilds = ['height','weight','bmi']
    if sort_by not in vaild_feilds:
        raise HTTPException(status_code=400,detail=f"invalid field selected from {vaild_feilds}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="invalid order select between ascending and decending")
    
    data=load_data()
    sort_order = True if order =="desc" else False
    
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    
    return sorted_data





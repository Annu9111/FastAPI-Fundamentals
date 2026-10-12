from pydantic import BaseModel,Field,computed_field
from fastapi.responses import JSONResponse 
from fastapi import FastAPI,Path,HTTPException,Query
from typing import Annotated,Literal
import json


app = FastAPI()


class Patient(BaseModel):
    id: Annotated[
        str,
        Field(
            ...,
            description="ID of the patient",
            examples=["P001", "P002"]
        )
    ]

    name: Annotated[
        str,
        Field(..., description="Name of the patient")
    ]

    city: Annotated[
        str,
        Field(..., description="City of the patient")
    ]

    age: Annotated[
        int,
        Field(..., gt=0, description="Age of the patient")
    ]

    gender: Annotated[
        Literal["male", "female", "other"],
        Field(..., description="Gender of the patient")
    ]

    height: Annotated[
        float,
        Field(..., gt=0, description="Height in meters")
    ]

    weight: Annotated[
        float,
        Field(..., gt=0, description="Weight in kilograms")
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    
    


def load_data():
    with open("02_patients.json","r") as f :
        data = json.load(f)
    return data    

def save_data(data):
    with open("02_patients.json",'w') as f:
        json.dump(data,f)
    
    

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
    
# @app.get('/patient/{patient_id}')
# def patient(patient_id : str=Path(...,description="Id required")):
#     data = load_data()
#     if patient_id in data:
#         return data[patient_id]
#     raise HTTPException(status_code=404,detail="patient not found")  
    
# @app.get('/sort')
# def sort_patient(sort_by:str = Query(...,description="sort on the basis of height,weight or bmi"),order:str=Query('asc',description="sort in ascending and decending order")):
#     vaild_feilds = ['height','weight','bmi']
#     if sort_by not in vaild_feilds:
#         raise HTTPException(status_code=400,detail=f"invalid field selected from {vaild_feilds}")
    
#     if order not in ['asc','desc']:
#         raise HTTPException(status_code=400,detail="invalid order select between ascending and decending")
    
#     data=load_data()
#     sort_order = True if order =="desc" else False
    
#     sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    
#     return sorted_data


@app.post('/create')
def create_patient(patient:Patient):
    #load existing data
    data=load_data()
    
    #check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400,detail='patient with this id is already exists')
    
    #new patient is added to the database
    data[patient.id]=patient.model_dump(exclude=['id'])
    
    #save into the json file
    save_data(data)
    
    return JSONResponse(status_code=201,content={'message':'patient create has successfully added'})
    



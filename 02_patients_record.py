from fastapi import FastAPI,Path
import json


app = FastAPI()

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
    return {'error':'patient not found'}    
    



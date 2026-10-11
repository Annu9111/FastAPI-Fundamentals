from fastapi import FastAPI
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



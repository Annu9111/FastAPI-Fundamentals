from fastapi import FastAPI
# from moc_detail import detail

app = FastAPI()

@app.get('/')
def home():
    return 'welcome to home page'

@app.get('/contact')
def home():
    return 'contact page'

# @app.get('/child/{child_id}')
# def getChild(child_id):
#     return {
#         "id":child_id
#     }

@app.get('/greet')
def greet(name:str):
    return f"hello {name}, how are you!"

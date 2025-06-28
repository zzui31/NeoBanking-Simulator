from fastapi import  FastAPI
from . import schemas

app = FastAPI()

@app.post('/user')
def create(request: schemas.User):
    return {'name' : request.name , 'email': request.email}
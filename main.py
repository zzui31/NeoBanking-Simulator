from fastapi import  FastAPI


app = FastAPI()

@app.post('/user')
def create():
    return 'creating'
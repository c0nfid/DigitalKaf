from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello_index():
    return {
        "message": "Hello, World!",
    }

@app.get('/hello/')
def hello_index():
    return {
        "message": "Hello, I'm Roman, student of RTU MIREA!",
    }
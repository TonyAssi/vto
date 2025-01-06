from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/vto")
async def vto():
    return {"greeting": "Hello, World! This is VTO.", "message": "Welcome to VTO!"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def read_login():
    return {"message": "Login page"}


@app.post("/register")
async def read_register():
    return {"message": "Register page"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "aura core online"}

import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

if_name == "_main__":

import uvicorn

uvicorn.run("main:app", host="0.0.0.0",

port=8000))

"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def reda_root():
    return {"message": "Hello, world"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item number {item_id}"}


@app.get("/ping")
def read_root():
    return {"status": "pang"}

@app.get("/greet/{name}")
def get_greeting(name: str):
    return {"message": f"Hello,{name}!"}


if __name__ == "__main__":
    uvicorn.run("test_venv:app", host="127.0.0.1", port=8000,reload=True)

"""

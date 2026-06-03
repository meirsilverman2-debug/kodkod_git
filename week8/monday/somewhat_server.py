# Exercise_3:

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/greet")
def greet_someone(name: str = "world"):
    return {"message": f"Hello {name}!"}

if __name__ == "__main__":
    uvicorn.run("somewhat_server:app", host="127.0.0.1", port=7700, reload=True)

from fastapi import FastAPI
from routers import items, users

app = FastAPI()


app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def check_health():
    return {"message": "I am alive!!!"}
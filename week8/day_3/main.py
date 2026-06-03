from fastapi import FastAPI
from logging_config import logging
app = FastAPI()

@app.get("/")
def get():
    return {"message": "server is running"}


@app.get("/hello")
def get_hello():
    return {"message": "Hello student"}

@app.get("/hello/{name}")
def get_hello(name):
    return {"message": f"Hello {name}"}
@app.get("/{username}/{item}/{price}")
def get_purchase(username, item, price):

    logging.info("start")
    if price != int(price):
        logging.error("error %s not int ")
        return

    elif int(price) < 0:
        logging.error("error price is nagative!!")
        return 
    
    elif int(price) > 1000:
        logging.warning("price is high")
        
    else:
        logging.info("Purchace successful:%s bought %s", username, item )
        return {"message": "Amazingly dun"}
from fastapi import FastAPI, HTTPException
from utils import IO
from logger_config import logger

app = FastAPI()



@app.get("/soldiers")
def get_all_soldiers():
    logger.info("The client ask to see all of the information about the soldiers system db")
    return IO.read()
    


@app.get("/soldiers/{id}")
def get_a_soldier(id: int):
    logger.info("The client want to see the information of a single soldier")
    soldiers = IO.read()
    for soldier in soldiers:
        if soldier["id"] != int(id):
            raise HTTPException(Status_code=404, detail=f"{id} does not exists!")
        return soldier
        


@app.post("/soldiers")
def create_a_soldier(budy: dict):
    logger.info("The client wants to register a new soldier named %s to the system ", budy["fullname"])
    data = IO.read()

    if budy["id"] in data["id"]:
        logger.error("id aleady exists in the db")
        raise HTTPException(status_code=409, detail= f"{budy[id]} already exsits")
    
    elif "fullname" not in budy or "rank" not in budy:
        logger.error("Missing field nams in the given budy!")
        raise HTTPException(status_code=400, detail="Requier f")

    IO.write(budy)
    logger.info("%swas added to the system",budy["fullname"])






@app.put("/soldiers/{id}")
def update_soldier(id: int, budy: dict):
    logger.info("The client wants to update the soldier with %d id", NotImplementedError)
    data = IO.read()
    
    for soldier in data:

        if soldier["id"] != id:
            logger.error("id does not exsits in db!")
            raise HTTPException(status_code=404, detail= f"{budy[id]} does not exsits")
        
        elif "fullname" not in budy or "rank not in budy":
            logger.error("missing a field in the given budy!")
            raise HTTPException(status_code=400, detail="Field 'name' is required")
        
        soldier["fullname"] = budy["fullname"]
        soldier["rank"] = budy["rank"]
        IO.write_update(data)
        logger.info("%d is now given an update", id)
       

@app.delete("/soldier/{id}")
def delete_soldier(id: int):
    logger.info("The client try to remove a soldier from the system")
    data = IO.read()

    for soldier in data:
        if soldier["id"] == id:
            logger.info("soldier has been deleted")
            data.remove(soldier)
            IO.write_update(data)
            logger.info("The soldier with the %d id was succeesfully removed", id)
            return {"message": "soldier has been deleted!"}

    logger.error("id does not exists in db!")
    raise HTTPException(status_code=404, detail=f"{id} dose not exsits in the db, and you cannot delete something that does not exsits")
               
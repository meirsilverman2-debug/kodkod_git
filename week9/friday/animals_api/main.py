from fastapi import FastAPI, HTTPException
from dal.animal_dal import Animal_DAL

app = FastAPI()

animal_dal = Animal_DAL()

@app.get("/")
def home():
    return {"message": "Animals API is runing"}

@app.post("/animals")
def create_one_animal(name: str, animal_type: str, age: int):
    animal_dal.create_animal(name, animal_type, age)

    return {"message": "Animal was created"}


@app.get("/animals")
def get_animals():
    return animal_dal.get_all_animals()


@app.get("/animals/{animal_id}")
def get_one_animal(animal_id: int):
    return animal_dal.get_animal_by_id(animal_id)


@app.put("/animals/{animals_id}")
def update_one_animal(animal_id: int, name: str, animal_type: str, age: int):
    animal_dal.update_animal(animal_id, name, animal_type, age)

    return {"message": "Animal was updated"}

@app.delete("/animals/{animal_id}")
def delete_animal(animal_id: int):
    animal_dal.delete_animal(animal_id)

    return {"message": "Animal was deleted"}
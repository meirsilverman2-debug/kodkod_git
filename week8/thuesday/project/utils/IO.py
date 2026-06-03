import json

def read() -> dict:

    with open(file="soldiers.json", mode="r", encoding="utf=8") as r_file:
        return json.load(r_file)
    

def write(budy: dict):

    data = read()
    data.append(budy)

    with open(file="soldiers.json", mode="w", encoding="utf-8") as w_file:
        json.dump(data, w_file, indent=4)


def write_update(data):
     
     with open(file="soldiers.json", mode="w", encoding="utf-8") as w_file:
        json.dump(data, w_file, indent=4)

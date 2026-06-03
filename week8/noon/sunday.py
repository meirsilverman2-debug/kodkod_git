# Level_1-basic:
# Exercise_1:

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/ping")
# def get_pong():
#     return {"status": "pong"}

# @app.get("/greet/{name}")
# def greeting(name: str):
#     return {"message": f"Hello, {name}!"}

# # Level_2-itemdaiate:

"""
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_service():
    return {"service": "my-api", "version": "1.0"}


@app.get("/users/admin")
def get_admin():
    return {"role": "admin", "access": "full"}


@app.get("/users/{user_id}")
def get_user_id(user_id):
    return {"user_id": f"{user_id}", "name": "Tzipi", "email": "silverman@.com"}

# Exercise_3:

@app.get("/calc/{a}/{op}/{b}")
def get_calc(a: int, op, b:int):
    d = {"operation": f"{op}"}

    if op == "+":
        d["result"] = a + b
    
    elif op == "-":
        d["result"] = a - b
    
    elif op == "*":
        d["result"] = a * b
    
    elif op == "div":
        if b != 0:
            d["result"] = a / b
    
    return d

# Exercise_4:


@app.get("/status")
def get_status():
    return {"datetime":f"{datetime.now()}", "server_name": "WEBUG"}
"""            
       
# Level_3-itemdaiate:
  
# # Exercise_5: 

from fastapi import FastAPI

app = FastAPI()

grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}


# @app.get("/students")
# def get_names():
#     for grade in grades:
#         grades[grade["name"]]
    

@app.get("/students")
def get_students():
    return grades

@app.get("/students/top")
def get_the_highest_student():
    top_student = 0
    d = 0

    for k in grades.keys():
        if grades[k]["grade"] > top_student:
           top_student = grades[k]["grade"]
           d  = grades[k] 
    return {"top":f"{d}"}
           
     

@app.get("/students/average")
def get_average():
    sum = 0
    for k in grades.keys():
        sum +=  grades[k]["grade"]

    return {"average": f"{sum / len(grades)}"}


@app.get("/students/count")
def get_the_amount_of_students():
    return {"student_amount": f"{len(grades)}"}


@app.get("/students/{student_id}")
def get_one_student(student_id: int):
    for k in grades.keys():
        if int(k) == student_id:
            return grades[k]
        

        
      
            
            


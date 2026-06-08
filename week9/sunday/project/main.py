from fastapi import FastAPI, HTTPException
from database.ddl_operations import create_database, drop_database, create_courses_table, create_student_table, create_teachers_table, rename_courses_table, run_query, drop_all_tables, add_phone_column
from database.connection import connection
import mysql.connector



app = FastAPI()


@app.post("/create")
def create_databases():
    create_database()



# Endpoint 1:

@app.post("/tables/creat")
def create_table():
    try:
        create_teachers_table()
        create_courses_table()
        create_student_table()

        return {"success": True, "message": "all tables created successfully"}
    
    except Exception as e:
        print(e)
        {"success": False,"error": "error message"}

# Endpoint 2:

@app.put("/students/add-phone/column")
def add_phone_column():
    try:
        add_phone_column()

        return {"success": True, "message": "all tables created successfully"}

    except Exception as e:
        print(e)
        {"success": False,"error": "error message"}

# Endpoint 3:

@app.delete("/tables")
def delete_tables():
    try:
        drop_all_tables()

        {"success": True,"message": "All tables deleted successfully"}

    except Exception as e:
        print(e)
        {"success": False,"error": "error message"}
    
        


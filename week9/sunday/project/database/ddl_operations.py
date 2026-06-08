# import mysql.connector 
from .connection import connection



# A good function so you won't need to create the query in the database

def run_query(query):

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(query)

    except Exception as e:
        print(e)

    finally:
        cursor.close()


# Level_1: database creator
#  
def create_database():

    query = "create database if not exists college ;"
    run_query(query)
    print("database was successfuly created.")

# Level_2: dleting database

def drop_database():

    query = "drop database ;" 
    run_query(query)
    print("database was successfully removed.")

# Level_3: students table (chart) creator

def create_student_table():

    query = "create table students (id int auto_increment primary key," \
    "full_name varchar(100)," \
    "email varchar(100)) ;" 

    run_query(query)
    print("Tha table of students was successfully created")

# Level_4: courses table (chart) creator

def create_courses_table():

    query = "create table courses (id int auto_increment primary key," \
    "course_name varchar(100)," \
    "price decimal(10,2)) ;"

    run_query(query)
    print("courses table was successfuly created")

# Level_5: teachers table creator

def create_teachers_table():

    query = "create table teachers (id int auto_incement primary key," \
    "full_name varchar(100)," \
    "salary decimal(10,2)) ;"

    run_query(query)

# Level_6: adding a column to a table

def add_phone_column():

    query = "alter table students add phone varchar(20) ;"

    run_query(query)
    print("A new column was successfully added to students (table/chart)")


# Level_7: adding another column to a table/chart

def add_birth_date_column():

    tabels = ["teachers", "students"]

    for table in tabels:
        query = f"alter table {table} add birth_date date " 
        run_query(query)
        print(f"{table} was successfuly created")

# Level_8: changing a spesific field in a database

def modify_email_column():
    query = " alter table students modify email varchar(255) ;"
    run_query(query)
    print("email was successfuly modify from max of 100 char to a max of 250 char")


# Level_9: changing the name of the table/char

def rename_courses_table():

    query = "alter table courses to training_courses ;"
    run_query(query)
    print("courses table was successfully renamed to training_courses congrachulation!!")


# Level_10: deleting one column from a table/chart

def drop_phone_column():

    tables = ["teachers", "students"]

    for table in tables:
        query = f"alter table {tables}  drop phone ; "
        run_query(query)
        print(f"Phone was successfully removed from {table} table ")


# Level_11: deleting a wholl table/chart

def drop_teachers_table():

    query = "drop table teachers ;"
    run_query(query)
    print("Teachers table was successfuly removed wow amazing")

# Level_12: deleting each and every table/chart from the database

def drop_all_tables():

    tables = ["teachers", "students", "training_courses"]

    for table in tables:
        query = f"drop table {table} ;"
        run_query(query)
        print(f"{table} was successfully deleted from data base")


from config import *


import mysql.connector

connection = mysql.connector.connect(
    host=HOST, # or "127.0.0.1"
    port=PORT,
    user=USER,
    password=PASSWORD,
    database=DATABASE
    
)

# cursor = connection.cursor(dictionary=True)
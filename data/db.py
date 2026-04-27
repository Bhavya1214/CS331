import mysql.connector

def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ramu@666",   # put your mysql password here if you have one
        database="email_system"
    )

    return conn
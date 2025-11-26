import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2345",
        database="hotel_chatbot"
    )
    cursor = db.cursor(dictionary=True)
    return db, cursor

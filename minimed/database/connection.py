# database/connection.py

import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="143.198.156.171",
            database='db_gonzalezj', 
            user='BD2021',
            password='BD2021itec' 
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"❌ ERROR al conectar a MySQL: {e}")
        return None

def close_connection(connection):
    """Cierra la conexión a la base de datos si está activa."""
    if connection and connection.is_connected():
        connection.close()
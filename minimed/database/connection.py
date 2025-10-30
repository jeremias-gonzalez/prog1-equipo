# database/connection.py

import sqlite3
import os

def get_connection():
    """Establece una conexión a la base de datos SQLite local."""
    try:
        # Obtener la ruta al archivo de base de datos
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, 'minimed_local.db')
        
        # Crear conexión
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
        
        return connection
    except sqlite3.Error as e:
        print(f"❌ ERROR al conectar a SQLite: {e}")
        return None

def close_connection(connection):
    """Cierra la conexión a la base de datos si está activa."""
    if connection:
        connection.close()

def init_database():
    """Inicializa la base de datos local si no existe."""
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            
            # Modificar el script SQL para ser compatible con SQLite
            current_dir = os.path.dirname(os.path.abspath(__file__))
            sql_file_path = os.path.join(current_dir, 'db_local_sqlite.sql')
            
            with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read()
            
            # Ejecutar cada sentencia SQL por separado
            for statement in sql_script.split(';'):
                if statement.strip():
                    try:
                        cursor.execute(statement)
                    except sqlite3.Error as e:
                        if "already exists" not in str(e):
                            print(f"Error en sentencia: {statement}")
                            print(f"Error: {e}")
            
            connection.commit()
            print("✅ Base de datos inicializada correctamente")
            
            cursor.close()
            close_connection(connection)
            
    except sqlite3.Error as e:
        print(f"❌ ERROR al inicializar la base de datos: {e}")

def test_connection():
    """Prueba la conexión a la base de datos y muestra información básica."""
    try:
        # Inicializar la base de datos
        print("Inicializando la base de datos...")
        init_database()
        
        # Probar la conexión
        print("\nProbando la conexión...")
        connection = get_connection()
        
        if connection:
            cursor = connection.cursor()
            
            # Obtener información de SQLite
            cursor.execute("SELECT sqlite_version()")
            db_version = cursor.fetchone()
            print(f"✅ Conectado a SQLite versión: {db_version[0]}")
            
            # Mostrar las tablas creadas
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            print("\nTablas creadas en la base de datos:")
            for table in tables:
                print(f"- {table[0]}")
            
            cursor.close()
            close_connection(connection)
            print("\n✅ Prueba de conexión completada con éxito")
            
    except sqlite3.Error as e:
        print(f"❌ Error durante la prueba: {e}")

# Si este archivo se ejecuta directamente, realizar la prueba de conexión
if __name__ == "__main__":
    test_connection()
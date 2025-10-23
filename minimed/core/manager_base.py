# core/manager_base.py

from database.connection import get_connection

class ManagerBase:
    
    def __init__(self, tabla):
        self.tabla = tabla
        self.conn = get_connection() 

    def get_by_id(self, id_val):
        if not self.conn: return None
        
        cursor = self.conn.cursor(dictionary=True)
        query = f"SELECT * FROM {self.tabla} WHERE id = %s"
        cursor.execute(query, (id_val,))
        
        resultado = cursor.fetchone() 
        cursor.close()
        return resultado
        
    def get_all(self):
        if not self.conn: return []
        
        cursor = self.conn.cursor(dictionary=True)
        query = f"SELECT * FROM {self.tabla}"
        cursor.execute(query)
        
        lista_resultados = cursor.fetchall()
        cursor.close()
        return lista_resultados
    
    def get_by_dni(self, dni_val):
        if self.tabla != "Persona":
            print("⚠️ Método get_by_dni debe usarse con la tabla Persona o Paciente.")
            return None
            
        if not self.conn: return None
        cursor = self.conn.cursor(dictionary=True)
        query = f"SELECT * FROM {self.tabla} WHERE dni = %s"
        cursor.execute(query, (dni_val,))
        return cursor.fetchone()
    
    
    def insert(self, datos):
        """LOGICA SQL INSERT MARCOS"""
        print(f"PENDIENTE: Insertar en {self.tabla}")
        return False

    def update(self, id_val, datos):
        """LOGICA SQL UPDATE BARROSO"""
        print(f"PENDIENTE: Actualizar {self.tabla}")
        return False

    def delete(self, id_val):
        """LOGICA SQL DELETE NACHO"""
        print(f"PENDIENTE: Eliminar de {self.tabla}")
        return False
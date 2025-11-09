# core/manager_base.py

def update(self, id_val, datos):
    """
    Actualiza un registro en la tabla basado en su ID.
    'id_val' es el ID del registro a actualizar.
    el diccionario con las columnas y los nuevos valores a actualizar es 'id_val'.
    """
    if not self.conn:
        print("⚠️ No hay conexión a la base de datos.")
        return False
    # En caso de estar vacío el diccionario, no hay nada que hacer
    if not datos:
        print("⚠️ No se proporcionaron datos para actualizar.")
        return False

    cursor = None
    try:
        cursor = self.conn.cursor()

        # La parte SET de la consulta se construye dinámicamente
        set_parts = [f"{key} = %s" for key in datos.keys()]
        set_clause = ", ".join(set_parts)
            
        # Lista de valores en el orden correcto
        valores = list(datos.values())
        valores.append(id_val) # Agregamos el ID al final para el where

        query = f"UPDATE {self.tabla} SET {set_clause} WHERE id = %s"
            
        cursor.execute(query, tuple(valores))
        self.conn.commit()
            
        if cursor.rowcount > 0:
            print(f"✅ Registro actualizado exitosamente en la tabla '{self.tabla}'.")
            return True
        else:
            print(f"⚠️ No se encontró ningún registro con el ID {id_val} para actualizar.")
            return False

    except Exception as e:
        print(f"❌ Error al actualizar en la tabla '{self.tabla}': {e}")
        self.conn.rollback() # Revierte los cambios si hubo un error
        return False
    finally:
        if cursor:
            cursor.close()

# Después del update, sigue la herramienta de búsqueda

def get_one_by_field(self, field_name, field_value):
   
    # Busca un único registro y lo devuelve basado en un campo específico.
    
    if not self.conn: return None
        
    cursor = self.conn.cursor(dictionary=True)
    query = f"SELECT * FROM {self.tabla} WHERE {field_name} = %s"
        
    try:
        cursor.execute(query, (field_value,))
        resultado = cursor.fetchone() 
        return resultado
    except Exception as e:
        print(f"❌ Error al buscar por campo '{field_name}': {e}")
        return None
    finally:
        cursor.close()            
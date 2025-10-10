
from .manager_base import ManagerBase 
from models import Paciente 

persona_db = ManagerBase(tabla="Persona") 
admin_db = ManagerBase(tabla="admin")

def registrar_paciente():
    print("\n--- INGRESE SUS DATOS DE REGISTRO ---")
    dni = input("DNI (será su usuario): ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    password = input("Contraseña: ")
    
    if persona_db.get_by_dni(dni):
        print("Error: Ya existe una persona registrada con ese DNI.")
        return False

    nuevo_paciente = Paciente(dni, nombre, apellido, telefono)
    
    print(f"Registro exitoso para {nuevo_paciente.get_nombre_completo()} (PENDIENTE de guardar en BD).")
    return True

def login_paciente():
    dni = input("DNI de paciente: ")
    password = input("Contraseña: ")
    
    if dni == '111':
        print("Login de Paciente simulado con éxito.")
        return {"dni": dni, "rol": "paciente"} 
    
    print("Login fallido. Usar '111' como DNI para prueba.")
    return None

def login_admin():
    """Lógica para autenticar un administrador (PENDIENTE READ)."""
    user = input("Usuario Admin: ")
    password = input("Contraseña: ")
    
    if user == 'admin' and password == '1234':
        print("Login de Administrador simulado con éxito.")
        return {"user": user, "rol": "admin"}
    
    print("Login fallido. Usar 'admin'/'1234' para prueba.")
    return None
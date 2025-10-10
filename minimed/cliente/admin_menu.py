
from core.admin_manager import AdminManager

def mostrar_menu_admin():
    print("\n--- MENÚ ADMINISTRADOR ---")
    print("1. Listar Médicos Registrados (READ)")
    print("2. Ver Turnos del dia (READ)")
    print("3. Gestión de Médicos (PENDIENTE INSERT/UPDATE/DELETE)")
    print("9. Cerrar Sesión")
    return input("Seleccione una opción: ")


def start_admin_menu(admin_data):
    manager = AdminManager(admin_data.get('user')) 
    
    print(f"\n¡Bienvenido/a, Administrador: {admin_data.get('user')}!")
    
    while True: # Iteración
        opcion = mostrar_menu_admin()

        if opcion == '1':
            manager.listar_medicos()
            
        elif opcion == '2':
       
            print("\n--- LISTADO DE TURNOS ---")
            fecha_input = input("Ingrese la fecha para el reporte (AAAA-MM-DD), o presione ENTER para ver TODOS: ").strip()
            
            if fecha_input:
                
                manager.ver_reporte_citas_del_dia(fecha=fecha_input)
            else:
            
                manager.ver_reporte_citas_del_dia(fecha=None) 
            
        elif opcion == '3':
            
            print("PENDIENTE: Gestión de Médicos (INSERT/UPDATE/DELETE).")
            pass
        elif opcion == '9':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        
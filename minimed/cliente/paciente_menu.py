# cliente/paciente_menu.py

from core.paciente_manager import PacienteManager

def mostrar_menu_paciente():
    print("\n--- MENÚ PACIENTE ---")
    print("1. Ver mis citas agendadas (READ)")
    print("2. Agendar nueva cita (PENDIENTE INSERT)")
    print("9. Cerrar Sesión")
    return input("Seleccione una opción: ")

def start_paciente_menu(paciente_data):
    manager = PacienteManager(paciente_data.get('dni')) 

    print(f"\n¡Bienvenido/a, Paciente con DNI: {paciente_data.get('dni')}!")

    while True: # Iteración
        opcion = mostrar_menu_paciente()

        if opcion == '1': # Alternativa
            manager.ver_mis_citas() 
        
        elif opcion == '2':
            # Tarea del compañero
            manager.agendar_nueva_cita({})
        
        elif opcion == '9':
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
#Fin del ciclo
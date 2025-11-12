from core.paciente_manager import PacienteManager

def mostrar_menu_paciente():
    print("\n--- MENÚ PACIENTE ---")
    print("1. Ver mis citas agendadas")
    print("2. Agendar nueva cita")
    print("3. Actualizar mis datos")
    print("4. Cerrar Sesión")
    return input("Seleccione una opción: ")

def start_paciente_menu(paciente_data):
    manager = PacienteManager(paciente_data.get('dni')) 

    print(f"\n¡Bienvenido/a,Ingresaste con tu DNI: {paciente_data.get('dni')}!")

    while True:
        opcion = mostrar_menu_paciente()

        if opcion == '1':
            manager.ver_mis_citas() 
        
        elif opcion == '2':
      
            manager.agendar_nueva_cita()
        
        elif opcion == '3':
            manager.actualizar_mis_datos()

        elif opcion == '4':
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
# core/paciente_manager.py

from .manager_base import ManagerBase

class PacienteManager:
    def __init__(self, paciente_dni):
        self.paciente_dni = paciente_dni
        self.turno_db = ManagerBase(tabla="Turnos")
        self.paciente_db = ManagerBase(tabla="Paciente")
        self.persona_db = ManagerBase(tabla="Persona") 

    def ver_mis_citas(self):
        print(f"\n--- Turnos de Paciente {self.paciente_dni} ---")
        
        citas = self.turno_db.get_all() 
        
        for i, cita in enumerate(citas):
            print(f"{i+1}. Fecha: {cita['fecha_turno']} | Hora: {cita['hora']} | Dr. ID: {cita['id_medico']}")
            
        if not citas:
            print("No se encontraron turnos.")
        
        return citas

    def agendar_nueva_cita(self, datos):
        print("PENDIENTE: Lógica de agendamiento (INSERT en Turnos).")
        pass

    def actualizar_mis_datos(self):
        print(f"\n--- Actualizar mis datos (Paciente {self.paciente_dni}) ---")
        print("Deje el campo vacío y presione ENTER para no cambiar el dato.")

        try:
            info_persona = self.persona_db.get_by_dni(self.paciente_dni)
            if not info_persona:
                print("Error: No se encontraron los datos de la persona.")
                return
            
            id_persona = info_persona.get('id')

            info_paciente = self.paciente_db.get_one_by_field('id_persona', id_persona)
            if not info_paciente:
                print("Error: No se encontraron los datos del paciente.")
                return
            
            id_paciente = info_paciente.get('id')
            
            nuevo_nombre = input(f"Nombre actual ({info_persona.get('nombre')}): ").strip()
            nuevo_apellido = input(f"Apellido actual ({info_persona.get('apellido')}): ").strip()
            nuevo_telefono = input(f"Teléfono actual ({info_paciente.get('telefono', 'N/A')}): ").strip()

            #Preparamos los diccionarios de datos para actualizar
            datos_persona = {}
            if nuevo_nombre:
                datos_persona['nombre'] = nuevo_nombre
            if nuevo_apellido:
                datos_persona['apellido'] = nuevo_apellido
                
            datos_paciente = {}
            if nuevo_telefono:
                datos_paciente['telefono'] = nuevo_telefono

            #Ejecutamos las actualizaciones
            if datos_persona:
                self.persona_db.update(id_persona, datos_persona)
            
            if datos_paciente:
                self.paciente_db.update(id_paciente, datos_paciente)
            
            if not datos_persona and not datos_paciente:
                print("No se ingresó ningún dato nuevo. No se realizó ninguna actualización.")
            
        except Exception as e:
            print(f"Ocurrió un error inesperado durante la actualización: {e}")
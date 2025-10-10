# core/paciente_manager.py

from .manager_base import ManagerBase

class PacienteManager:
    def __init__(self, paciente_dni):
        self.paciente_dni = paciente_dni
        self.turno_db = ManagerBase(tabla="Turnos")
        self.paciente_db = ManagerBase(tabla="Paciente") 

    def ver_mis_citas(self):
        print(f"\n--- Turnos de Paciente {self.paciente_dni} ---")
        
        citas = self.turno_db.get_all() 
        
        for i, cita in enumerate(citas):
            print(f"{i+1}. Fecha: {cita['fecha_turno']} | Hora: {cita['hora']} | Dr. ID: {cita['id_medico']}")
            
        if not citas:
            print("No se encontraron turnos.")
        
        return citas

    def agendar_nueva_cita(self, datos):
        """(TAREA  DE BARROSO)."""
        print("PENDIENTE: Lógica de agendamiento (INSERT en Turnos).")
        pass
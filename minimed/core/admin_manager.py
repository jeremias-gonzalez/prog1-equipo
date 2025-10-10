
from .manager_base import ManagerBase

class AdminManager:
    def __init__(self, admin_user):
        self.admin_user = admin_user
        self.medico_db = ManagerBase(tabla="Medico")
        self.turno_db = ManagerBase(tabla="Turnos")
        self.persona_db = ManagerBase(tabla="Persona") 

    def ver_reporte_citas_del_dia(self, fecha=None):
        
        if fecha:
            titulo = f"Turnos por Fecha: {fecha}"
            filtro_sql = "WHERE T.fecha_turno = %s"
            params = (fecha,)
        else:
            titulo = "Mostrar TODOS los Turnos"
            filtro_sql = "" 
            params = ()
            
        print(f"\n--- {titulo} ---")
        
        if not self.turno_db.conn: return []

        cursor = self.turno_db.conn.cursor(dictionary=True)
     
        query = f"""
        SELECT 
            T.fecha_turno, 
            T.hora, 
            P_PACIENTE.nombre AS nombre_paciente, 
            P_PACIENTE.apellido AS apellido_paciente,
            P_MEDICO.nombre AS nombre_medico, 
            P_MEDICO.apellido AS apellido_medico,
            ME.especializacion  -- <<--- CORREGIDO: Usando el alias correcto ME
        FROM Turnos AS T
        JOIN Paciente AS PA ON T.id_paciente = PA.id
        JOIN Persona AS P_PACIENTE ON PA.id_persona = P_PACIENTE.id
        JOIN Medico AS ME ON T.id_medico = ME.id
        JOIN Persona AS P_MEDICO ON ME.id_persona = P_MEDICO.id
        {filtro_sql}
        ORDER BY T.fecha_turno DESC, T.hora ASC
        """
        
        try:
            cursor.execute(query, params)
            citas = cursor.fetchall() 
        except Exception as e:
            print(f"Error al ejecutar la consulta de turnos: {e}") 
            return []
        finally:
            cursor.close()

        if citas:
            print(f"Total de turnos encontrados: {len(citas)}")
            for i, cita in enumerate(citas):
                print("-" * 50)
                print(f"Turno {i+1} | Fecha: {cita['fecha_turno']} Hora: {cita['hora']}")
                print(f"  Paciente: {cita['nombre_paciente']} {cita['apellido_paciente']}")
                print(f"  Médico: Dr. {cita['apellido_medico']} ({cita['especializacion']})")
        else:
            print("No se encontraron turnos bajo este criterio.")
            
        return citas

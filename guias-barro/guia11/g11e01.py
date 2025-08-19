class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
"""
class Alumno:
    def __init__(self, nombre, apellido): # método constructor
        self.nombre = nombre # self.nombre es un atributo ...
        self.apellido = apellido # ... y self.apellido otro atributo
        inicial = nombre[0].lower() # variable local
        # y self.mail aunque no viene de parámetros, también es un atributo:
        self.mail = f'{inicial}.{apellido.lower()}@itecriocuarto.org.ar'

    def nombre_completo(self): # método
        return f'{self.nombre} {self.apellido}'

    def promedio(self, *args): # otro método
        return sum(args) / len(args)

alumno1 = Alumno('Juan', 'Torres') # instanciación (creación del objeto)
print(f'El alumno {alumno1.nombre_completo()} tiene este mail: {alumno1.mail}')
print(f'Y su promedio es {alumno1.promedio(4,5,7)}')
"""
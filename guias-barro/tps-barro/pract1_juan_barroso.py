"""
#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

nombre_completo = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana", "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"]

Departamento = ["Logística", "Desarrollo", "Desarrollo", "Logística", "Administración", "Logística", "Desarrollo"]
Fecha_de_Nacimiento = ["15/05/1943", "07/04/1984", "10/02/1971", "21/12/1967", "30/01/1982", "30/08/1995", "18/07/1959"]

for i in nombre_completo:
    lol = i.split(", ")
    nombres_i = lol[1][0]
    apellidos = lol[0][:11]
    print(f'{nombres_i}, {apellidos}')

#2) Decir cuál es el nombre de pila más largo.

personas = [
    "Torres, Ana", 
    "Hudson, Kate", 
    "Quesada, Benicio", 
    "Campoamores, Susana", 
    "Santamaría, Carlos", 
    "Skarsgard, Azul", 
    "Catalejos, Walter"    
]

nombre_mas_largo = ""

for n in personas:
    pila = n.split(", ")[1]
    if len(pila) > len(nombre_mas_largo):
        nombre_mas_largo = pila
print(f"El nombre mas largo es: {nombre_mas_largo}")
"""

#3) Mostrar el promedio de edad de las personas del Departamento de Logística
# Datos

nombres = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana", "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"]

departamentos = ["logística", "Desarrollo", "Desarrollo", "logística", "Administración", "logística", "Desarrollo"]

fechas_de_nacimiento = ["15/05/1943", "07/04/1984", "10/02/1971", "21/12/1967", "30/01/1982", "30/08/1995", "18/07/1959"]

suma_edades = 0
cantidad_personas = 0

for i in range(len(nombres)):
    if departamentos[i] == "logística":
        fecha = fechas_de_nacimiento[i]
        partes = fecha.split("/")
        año_nac = int(partes[2])
        edad = 2024 - año_nac
        suma_edades += edad
        cantidad_personas += 1

promedio = suma_edades / cantidad_personas

print("El promedio de edad de las personas del Departamento de Logística es de", int(promedio), "años")

#11) Cargar los nombres y fechas de nacimiento de varias personas,
# luego recorrer y mostrar los nombres de los mayores de edad.
personas = [

]

while True:
    diccionario = {}
    diccionario["Nombre"] = input('Ingrese un nombre: ')
    diccionario["Nacimiento"] = int(input('Ingrese el año de nacimiento: '))
    pregunta = input('¿Desea ingresar otro nombre y año de nacimiento? (Si/No): ')
    personas.append(diccionario)
    if pregunta == "No":
        break
for i in personas:
    resta = 2025 - i["Nacimiento"]
    if resta > 18:
        print(f'La/Las persona/s mayor/es de edad es/son: {i["Nombre"]}')
        
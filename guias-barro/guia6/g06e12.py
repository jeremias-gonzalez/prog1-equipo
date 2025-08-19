#12) Crea una lista a mano con al menos 3 elementos, 
# el primero de ellos debe ser el diccionario persona que obtuvimos como salida en el ejercicio número 5. 
# Los siguientes elementos de la lista deben ser diccionarios similares (tipo registro). 
# Luego muestra los nombres de todas las ciudades y el promedio de los años de experiencia de los profesionales.

personas = [
    {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Rio Cuarto', 'Profesión': 'Ingeniero', 'Años de experiencia': 10},
    {'nombre': 'Miguel', 'edad': 25, 'ciudad': 'Córdoba', 'Profesión': 'Ingeniero', 'Años de experiencia': 6},
    {'nombre': 'Luis', 'edad': 42, 'ciudad': 'La Plata', 'Profesión': 'Ingeniero', 'Años de experiencia': 15}
]

for ciudad in personas:
    print(ciudad["ciudad"])

total = 0
lista_promedios = []
for i in personas:
    total += i['Años de experiencia']
lista_promedios.append(total / 3)

"""
for i in lista_promedios:
    print(i / 3)
"""
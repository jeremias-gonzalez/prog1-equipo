#Cargar en dos listas paralelas nombres y sueldos. 
#Recorrer las listas cargadas
#e ir mostrando los nombres de las personas que ganan más de $2_850_000.


lista_nombres = []
lista_sueldos = []

while True:
    nombres = input('Ingrese un nombre: ')
    lista_nombres.append(nombres)

    sueldos = int(input('Ingrese el sueldo: $'))
    lista_sueldos.append(sueldos)
    
    pregunta = input('¿Quiere ingresar mas personas y salarios?: ')
    if pregunta == "No":
        break

ganan_mas = []
for i in range(len(lista_nombres)):
    if lista_sueldos[i] > 2850000:
        ganan_mas.append(lista_nombres[i])
print(f'Los que ganan más de $2.850.000 son: {", ".join(ganan_mas)}')


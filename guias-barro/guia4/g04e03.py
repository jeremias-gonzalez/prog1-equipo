#3) Primer bucle: Almacenar en dos listas paralelas, nombres y sexos de personas
# hasta que el usuario diga que no hay más.
lista_nombres = []
lista_sexos = []

while True:
    nombre = input("Ingrese su nombre: ")
    lista_nombres.append(nombre)
    sexo = input("Ingrese su sexo: ")
    lista_sexos.append(sexo)
    pregunta = input("Desea ingresar otro nombre y sexo? (Si/No): ")
    if pregunta == "No":
        break

#Segundo bucle: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
lista_mujeres = []

for i in range(len(lista_nombres)):
    if lista_sexos[i] == "M":
        lista_mujeres.append(lista_nombres[i])

#Tercer bucle: Mostrar los elementos de la lista resultante y la cantidad.
contador = 0
for i in lista_mujeres:
    contador += 1
print(lista_mujeres)
print(f'La cantidad de mujeres son: {contador}')

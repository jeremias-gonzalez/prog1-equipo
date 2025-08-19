# Primer bucle: Almacenar en dos listas paralelas, nombres y sexos de personas 
# hasta que el usuario diga que no hay más. 

nombres = []
sexos = []

while True:
    nombre = input('Ingrese un nombre: ')
    sexo = input('Ingrese un sexo (masculino/femenino): ')
    pregunta = input('Hay más personas y sexos para agregar?(s/n): ')
    if pregunta == 'n':
        break
    nombres.append(nombre)
    sexos.append(sexo)
print (nombres)
print (sexos)

# Segundo bucle: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 


nueva_lista = []
    
for i in range(len(nombres)):
    if sexos[i] == "femenino":
        nueva_lista.append(nombres[i])
print(nueva_lista)

#Tercer bucle: Mostrar los elementos de la lista resultante y la cantidad.

cantidad = len(nueva_lista)

for i in range(cantidad):
    print(nueva_lista[i])
print(cantidad)
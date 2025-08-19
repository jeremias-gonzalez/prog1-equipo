#6) Ingresar nombres en una lista sin repetir (por teclado), 
# luego buscar un nombre (por recorrido) 
# y de encontrarlo decir en qué posición está.
lista_nombres = []

while True:
    nombre = input('Ingrese un nombre (Sin repetir): ')
    lista_nombres.append(nombre)
    pregunta = input('Desea ingresar otro nombre? (Si/No): ')
    if pregunta == "No":
        break

buscar_nombre = input('¿Qué nombre desea buscar?: ')

for i in range(len(lista_nombres)):
    if buscar_nombre in lista_nombres[i]:
        print(f'El nombre {buscar_nombre} está en la posicion {i+1} ')
if buscar_nombre not in lista_nombres[i]:
        print(f'El nombre {buscar_nombre} no está en la lista')
   
    

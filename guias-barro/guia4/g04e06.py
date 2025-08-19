#6) Ingresar nombres en una lista sin repetir (por teclado), 
# luego buscar un nombre (por recorrido) 
# y de encontrarlo decir en qué posición está.

lista_nombres = []

while True:
    nombre = input('Ingrese un nombre (Sin repetir): ')
    lista_nombres.append(nombre)
    pregunta = input('¿Desea ingresar otro nombre? (Si/No): ')
    
    if pregunta == "No":
        break

buscar_nombre = input('¿Qué nombre desea buscar?: ')
contador = 1
for i in range(len(lista_nombres)):
    if buscar_nombre == lista_nombres[i]:
        contador += i
print(f'El nombre {buscar_nombre} está en la posición {contador}')
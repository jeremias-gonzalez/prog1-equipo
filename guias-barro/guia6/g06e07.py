#7) Crea un diccionario con varios países y capitales. 
# Pide al usuario que ingrese el nombre de un país y muestra la capital correspondiente si existe en el diccionario. 
# Si no existe, muestra un mensaje indicando que el país no se encuentra en el diccionario.

Países_y_capitales = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Alemania": "Berlin", "Inglaterra": "Londres", "España": "Madrid"}

buscar = input("Ingrese un país: ")

for k, v in Países_y_capitales.items():
    if buscar == k:
        print(v)

if buscar not in Países_y_capitales:
    print("¡Ese país no se encuentra en el diccionario!")
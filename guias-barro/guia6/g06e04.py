#4) Crea un diccionario sin carga (con una iteración automática) 
# donde las claves sean números del 1 al 5 y los valores sean sus respectivos cuadrados. 
# Luego, muestra el diccionario.

dic_numeros = {}
for i in range(1, 6):
    dic_numeros[i] = i ** 2
print(f"El cuadrado de los mismo valores son: {dic_numeros}")
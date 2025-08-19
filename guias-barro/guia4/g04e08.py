#8) Cargar una lista con números. 
# Invertir los elementos sin usar otra lista. Sin usar reverse.

lista_numeros = []

while True:
    numeros = input('Ingrese un número: ')
    lista_numeros.append(numeros)
    pregunta = input('Desea ingresar otro número?(Si/No): ')

    if pregunta.lower() == "No":
        break

    
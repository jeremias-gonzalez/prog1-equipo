#8) Cargar una lista con números. 
# Invertir los elementos sin usar otra lista. Sin usar reverse.

lista_numeros = []

while True:
    numeros = int(input('Ingrese un número: '))
    lista_numeros.append(numeros)
    pregunta = input("¿Desea ingresar otro número? (Si/No): ").lower()
    if pregunta == "no":
        break
    elif pregunta != "si":
        print("¡La respuesta debe ser 'Si' o 'No'!")

for i in range(len(lista_numeros) // 2):
    lista_numeros[i], lista_numeros[-(i+1)] = lista_numeros[-(i+1)], lista_numeros[i]
print(lista_numeros)

    
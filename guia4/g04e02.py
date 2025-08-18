# Cargar letras en una lista hasta que el usuario ingrese un asterisco. 
# Luego hacer otra iteración para contar las vocales.
# Al final mostrar el total.

lista_letras = []
vocales = ["a", "e", "i", "o", "u"]
contador = 0


while True:
    letra = input("Ingrese una letra: ")
    lista_letras.append(letra)
    if letra == "*":
        break

for i in lista_letras:
    if i in vocales:
        contador += 1
print(contador)


        
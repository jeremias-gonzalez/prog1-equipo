#Cargar letras en una lista hasta que el usuario ingrese un asterisco.
lista_letras = []

while True:
    letra = input("Ingrese una letra: ")
    if letra == "*":
        break
    lista_letras.append(letra)

# Luego hacer otra iteración para contar las vocales.
contador = 0

lista_vocales = ['a', 'e', 'i', 'o', 'u']

for i in lista_letras:
    if i in lista_vocales:
        contador += 1      
print(contador)

# Al final mostrar el total.

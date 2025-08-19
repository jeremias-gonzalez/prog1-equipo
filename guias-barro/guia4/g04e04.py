#4) Dada una lista con números, crear otra con los cuadrados de esos valores.

lista_numeros = [2, 3, 5, 6, 7]
lista_cuadrados = []

"""
for i in lista_numeros:
    lista_cuadrados.append(i ** 2)
print(lista_cuadrados)
"""
lista_cuadrados = [i ** 2 for i in lista_numeros]
print(lista_cuadrados)

#Guardar en una lista los números pares mayores que 0 y menores que 31.

numeros_pares = []

for i in range(31):
    if i % 2 == 0 and i > 0:
        numeros_pares.append(i)
print(numeros_pares)


n_pares =  [i for i in range(31) if i % 2 == 0 and i > 0]
print(n_pares)
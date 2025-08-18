#1) Pedir el ingreso de 10 números.
numeros = []

for i in range(10):
    n = int(input("Ingrese un número: "))
    # Contar los mayores de 23 y almacenar los que cumplen la condición. 
    if n > 23:
        numeros.append(n)
# Mostrar la cantidad y los números guardados.
print(numeros)


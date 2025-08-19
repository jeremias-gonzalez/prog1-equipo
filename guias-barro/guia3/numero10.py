#10) Ingresar 7 números enteros.
# y en el caso de que sean naturales de una sola cifra mostrar un cartel en cada uno.


for i in  range(0, 7):
    numeros = int(input("Ingrese un número: "))
    if numeros < 10: 
        print("Es de una sola cifra")
print(numeros)

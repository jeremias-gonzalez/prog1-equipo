"""
contador = 0
resultado = 1

while resultado == 1:
    auto = input("Ingrese el auto: ")
    precio = int(input("Ingrese el precio: "))
    if 27460000 <= precio <= 33850000:
        contador += 1
        resultado = input("Queres seguir cargando autos? Ingrese 1 para seguir o Ingrese 0 para no ingresar más: ")
print(f'{contador} autos valen más entre 27460000 y 33850000')
"""

contador = 0
while True:
    tutu = input('Ingrese el coche: ')
    precio = int(input('Ingrese el precio del tutú: '))
    if 27460000 <= precio <= 33850000:
        contador += 1

    resultado = input('Desea ingresar otro coche?(si/no): ')
    if resultado == "no":
        break

print(f'{contador} autos valen más entre $27460000 y $33850000')

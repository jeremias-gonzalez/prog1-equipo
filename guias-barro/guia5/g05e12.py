#12) Pedir dos nombres y edades respectivas 
#y luego construir una sola cadena con un texto que muestre el nombre del mayor y cuanto le lleva al menor.
#(Ejemplo: entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')

cadena_nombres = ""
cadena_edades = ""

for i in range(2):
    nombres = input('Ingrese un nombre: ')
    edades = input('Ingrese una edad: ')
    cadena_nombres += nombres + " "
    cadena_edades += edades + " "
lista_nombres = cadena_nombres.strip().split(" ")
lista_edades = cadena_edades.strip().split(" ")
n1 = int(lista_edades[0])
n2 = int(lista_edades[1])

if n1 > n2:
    print(f'{lista_nombres[0]} es mayor que {lista_nombres[1]}, y le lleva {n1 - n2} años.')
elif n2 > n1:
    print(f'{lista_nombres[1]} es mayor que {lista_nombres[0]}, y le lleva {n2 - n1} años.')
else:
    print(f'{lista_nombres[0]} y {lista_nombres[1]} ¡Tienen la misma edad!')
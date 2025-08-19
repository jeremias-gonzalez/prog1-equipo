#Pedir dos números
#Decir cual es mayor
#En caso de ser iguales poner una salida que diga 'ingresaste dos veces el mismo número'

n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese otro número: '))

if n1 > n2:
	print(f'El número {n1} es mayor que el número {n2}')
elif n2 > n1:
	print(f'El número {n2} es mayor que el número {n1}')
else:
	print('Ingresaste dos veces el mismo número')

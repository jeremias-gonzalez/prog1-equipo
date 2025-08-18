#Pedir dos números

n1 = int(input('Ingresá un número guacho: '))
n2 = int(input('Ingreese otro número maestro: '))

#Elija una opción
jijo = input('Elija una opción + o -: ')

suma = n1 + n2
resta = n1 - n2 

if jijo == "+":
	print(f'La suma de los valores {n1} y {n2} es: {suma}')
elif jijo == "-":
	print(f'La resta de los valores {n1} y {n2} es: {resta}')


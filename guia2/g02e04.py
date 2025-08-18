#Pedir un nombre
nombre = input('Ingrese un nombre: ')

kj = input('Usted es mayor o menor de edad?: ')

if kj == "Mayor" or kj == "mayor":
	print(f'lol, {nombre} sos mayor de edad')
elif kj == "Menor" or kj == "menor":
	print(f'lol, {nombre} sos menor de edad')
else:
	print("No está dentro de los parámetros, por favor, ingrese mayor o menor, pendejo casta.")
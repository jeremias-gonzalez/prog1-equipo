nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))

myam = int(20000*0.80)
m = int(20000)

if edad >= 5 and edad <= 10:
	print(f'{nombre} de {edad} años tiene un costo del pasaje de ${myam}')
elif edad > 10 and edad < 65:
	print(f'{nombre} de {edad} años tiene un costo del pasaje de ${m}')
elif edad >= 65 and edad < 100:
	print(f'{nombre} de {edad} años tiene un costo del pasaje de ${myam}')
else:
	print('Tas muelto bro xd')



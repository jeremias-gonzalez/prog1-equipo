nombre = input('Hola usuario, ingrese su nombre: ')
print(f'Hola {nombre}, le damos la bienvenida a la calculadora de descuento, por favor, indique el nombre del producto del cual quiere saber el descuento.')

#Solicitar al usuario el nombre del producto
producto = input('Ingrese el nombre del producto: ')

#Solicitar el precio original
precio = float(input('Ingrese el valor del producto: '))

#Solicitar el precio de descuento que quiere el usuario
descuento = float(input('Indique el valor de descuento (no sobrepase el limite del 50%): '))
if descuento > 50:
	print("Error! El descuento no puede ser mayor a: 50%")
else:
#Calcular dependiendo el porcentaje
	porcentaje = precio - (precio * (descuento / 100))

	print(f'Hola {nombre}, el valor original del producto "{producto}" es de ${precio:.2f}.')
	print(f'Con un descuento del {descuento}%, el precio final es de ${porcentaje:.2f}.')

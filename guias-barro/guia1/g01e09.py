# Calculadora de descuento: Solicitar al usuario el nombre del producto, el precio original y el porcentaje de descuento. 
# Calcular y mostrar el precio final después del descuento.
# Salida ejemplo: Hola Juan! El producto Auriculares Behringer de precio original $30000 te queda en $27000 con el descuento del 10%

nombre = input('Hola usuario, ingrese su nombre: ')
print(f'Hola {nombre}, le damos la bienvenida a la calculadora de descuento, por favor, indique el nombre del producto del cual quiere saber el descuento.')

producto = input('Ingrese el nombre del producto: ')

precio = float(input('Ingrese el valor del producto: '))

descuento = float(input('Indique el valor de descuento (no sobrepase el limite del 50%): '))
if descuento > 50:
	print("Error! El descuento no puede ser mayor a: 50%")
else:
	porcentaje = precio - (precio * (descuento / 100))

	print(f'Hola {nombre}, el valor original del producto {producto} es de ${precio:.2f}.')
	print(f'Con un descuento del {descuento}%, el precio final es de ${porcentaje:.2f}.')

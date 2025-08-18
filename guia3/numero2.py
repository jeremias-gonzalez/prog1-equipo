#2) Pedir el ingreso de 5 números. 
# Contar los mayores de 23. Mostrar el resultado.

for i in range(5):
	numero = int(input("Ingrese un número: "))
	if numero > 23:
		print(f"El número {numero} es mayores a 23")
	else:
		print(f'{numero} no es mayor a 23')
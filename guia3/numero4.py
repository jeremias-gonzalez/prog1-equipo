
personas = int(input("Ingrese la cantidad de personas: "))
total = 0

for i in range(personas):
	sueldo = int(input(f"Ingrese el salario de la persona numero {i+1}: "))
	total = total + sueldo
print(f"La suma de los montos es de ${total}")

"""
contador = 0
total_sueldos = 0

while True:
	sueldo = int(input("Ingrese el sueldo del empleado: "))
	total_sueldos += sueldo
	contador += 1
	respuesta = str(input("Desea ingresar otro sueldo? (si/no): "))
	if respuesta == "no":
		break
print(f"La cantidad de empleados son: {contador}")
print(f'EL total de sueldos es: ${total_sueldos}')
"""



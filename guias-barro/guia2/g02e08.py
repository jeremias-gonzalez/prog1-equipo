print('De quien quiere saber su sueldo? Elija a Juan, Marcos, o Jeremías')
empleados = ["Juan", "Marcos", "Jeremías"]
nombre = input('Ingrese un nombre: ')
if nombre not in empleados:
	print('No es un nombre que aparece en la lista')
	exit()

sueldo = int(1000000)
sueldoj= int(0)
sueldom= int(-1)

año = int(input('Año de ingreso: '))

antigüedad = int(input('Cuántos años de antiguedad tenés: '))

ausente = int(input('Cuántos días te ausentaste desde tu fecha de ingreso hasta la actualidad?: '))

if nombre == "Juan" and antigüedad >= 5:
	print(f'{nombre}: Ausentismo={ausente} / Año de Ingreso={año} / Sueldo= ${sueldo*1.30}')
elif nombre == "Juan" and antigüedad < 5:
	print(f'{nombre}: Ausentismo={ausente} / Año de Ingreso={año} / Sueldo= ${sueldo}')

if nombre == "Marcos" and antigüedad >=5:
	print(f'{nombre}: Ausentismo={ausente} / Año de Ingreso={año} / Sueldo= ${sueldom}')
elif nombre == "Marcos" and antigüedad < 5:
	print(f'{nombre}: Ausentismo={ausente} / Año de Ingreso={año} / Sueldo= ${sueldom-sueldo}')

if nombre == "Jeremías" and antigüedad >=5:
	print(f'{nombre}: Ausentismo={ausente} / Año de Ingreso={año} / Sueldo= ${sueldoj} kjjjjjjjjj domado el gil laburante')
elif nombre == "Jeremías" and antigüedad < 5:
	print(f'{nombre}: Ausentismo={ausente} / Año de Ingreso={año} / Sueldo= ${sueldom} como esclabura el gordito')

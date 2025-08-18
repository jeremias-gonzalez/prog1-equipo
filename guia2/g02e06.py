#Ingrese su nombre
nombre = input('Ingrese su nombre: ')

#Carrera a la que se inscribe
print(f'{nombre}, te puedes inscribir a las siguientes carreras: Mecatronica, Desarrollo de Software, y Hotelería y Turismo')
carreras_disponibles = "Mecatrónica", "Desarrollo de Software", "Hotelería y Turismo"
carrera = input('Nombre de la carrera a la que se quiere inscribir: ')

if carrera not in carreras_disponibles:
	print(f'Esa carrera no está disponible aquí >:(!')
	exit()

#Localidad donde vive
localidad = input('Por favor, ingrese la localidad a la que pertenece: ')

#Calcular costos
cuota = int(100000)
mec = int(100000*0.85)
hot = int(100000*0.95)

if carrera == "Mecatrónica" and localidad == "Río Cuarto":
	print(f'{nombre}, estudiante de {carrera}, de la localidad de Río Cuarto tiene una cuota de ${cuota}')
elif carrera == "Mecatronica" and localidad != "Río Cuarto":
	print(f'{nombre}, estudiante de {carrera}, de la localidad de {localidad} tiene una cuota de ${mec}')

if carrera == "Hotelería y Turismo" and localidad == "Río Cuarto":
	print(f'{nombre}, estudiante de {carrera}, de la localidad de Río Cuarto tiene una cuota de ${cuota}')
elif carrera == "Hotelería y Turismo" and localidad != "Río Cuarto":
	print(f'{nombre}, estudiante de {carrera}, de la localidad de {localidad} tiene una cuota de ${hot}')


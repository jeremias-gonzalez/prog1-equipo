
#Calculadora de envío: Solicitar el peso de un paquete en kg y la distancia en km y calcular el costo total del envío según el siguiente tarifario:
#0-1 kg: $150 base + $10 por km
#1-5 kg: $300 base + $20 por km
#5-10 kg: $450 base + $30 por km
#10 kg: Mensaje de salida: No enviamos paquetes de 10 kg o más
#Salida ejemplo: El costo total de envío de tu paquete de 2 kg a una distancia de 200 km es de $4300


#solicitar peso de un paquete en kg
pak = input("Ingrese por favór el peso del paquete: ")
pak = int(pak)

#Solicitar la distancia en Km
distancia = int(input("Ingrese la distancia en Km: "))

if pak >= 0 and not pak != 1:
	print(f'El costo total de tu paquete de {pak} Kg a una distancia de {distancia} Km es de ${distancia * 10 + 150}')

elif pak > 1 and not pak != 5:
	print(f'El costo total de tu paquete de {pak} Kg a una distancia de {distancia} Km es de ${(distancia * 20) + 300}')

elif pak > 5 and pak <= 9: 
	print(f'El costo total de tu paquete de {pak} Kg a una distancia de {distancia} Km es de ${(distancia * 30) + 450}')
else:
	print('No enviamos paquetes de 10 kg o más')



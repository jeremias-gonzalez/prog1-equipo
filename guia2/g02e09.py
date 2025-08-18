print(f'Bienvenido a la calculadora de IMC (Índice de Masa Corporal), por favor, indique su peso y altura.')
altura = float(input('Ingrese aquí su altura en metros: '))
peso = int(input('Ahora ingrese su peso en Kg: '))
resultado = peso / (altura ** 2)
print(f'Usted mide {altura} metros y pesa {peso} Kg, por lo que su IMC marca: {resultado:.2f}')

if resultado < 18.5:
	print("Sos flac@")
elif resultado >= 18.5 and resultado < 24.9:
	print("Peso normalito")
elif resultado >= 24.9 and resultado <= 29.9:
	print("sobrepeso")
elif resultado >= 30:
	print("Bianca")

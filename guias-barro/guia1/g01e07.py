# Calculadora de IMC (Índice de Masa Corporal): Solicitar al usuario su peso en kilos y su altura en metros. 
# Calcular el IMC utilizando la fórmula: peso dividido el cuadrado de la altura.
# Salida ejemplo: Para tu peso de 93 kilos y tu altura de 1.73 metros tu Índice de Masa Corporal (IMC) es 31.07


print('Bienvenido a la calculadora de IMC (Índice de Masa Corporal), por favor, indique su peso y altura.')
altura = float(input('Ingrese aquí su altura en metros: '))
peso = int(input('Ahora ingrese su peso en Kg: '))
resultado = peso / (altura ** 2)
print(f'Usted mide {altura} metros y pesa {peso} Kg, por lo que su IMC marca: {resultado:.2f}')

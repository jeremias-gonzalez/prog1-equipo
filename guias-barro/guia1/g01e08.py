# Conversor de grados Celsius a Fahrenheit: Pedir el ingreso de una temperatura en Celsius (el formato que usamos nosotros) 
# Y convertirla a Fahrenheit (el formato que usa Estados Unidos). Buscar la fórmula.
# Salida ejemplo: 30 grados Celsius equivalen a 86 Fahrenheit

print(f'Bienvenido al conversor de grados Celsius a grados Farenheit, por favor, ingrese la temperatura en Celsius.')
celsius = float(input('Ingrese la temperatura en grados Celsius aquí: ')) 

farenheit = (celsius * 9/5) + 32

print(f'{celsius} grados celsius equivalen a: {farenheit:.2f} grados Farenheit')

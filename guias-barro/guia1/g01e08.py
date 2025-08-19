print(f'Bienvenido al conversor de grados Celsius a grados Farenheit, por favor, ingrese la temperatura en Celsius.')
celsius = float(input('Ingrese la temperatura en grados Celsius aquí: ')) #Pedir la temperatura en celsius

#Transformar la temperatura a grados farenheit
farenheit = (celsius * 9/5) + 32

print(f'{celsius} grados celsius equivalen a: {farenheit:.2f} grados Farenheit')

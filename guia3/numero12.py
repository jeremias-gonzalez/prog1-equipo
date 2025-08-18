# Ingresar la lluvia caída en milímetros para cada día de la semana. 
# Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.

lluvia = 0
dias_sin_lluvia = 0
for i in range(1,8):
    lluvia_caida = float(input(f"Ingrese la cantidad de milimetros caidos del Día {i}: "))
    if lluvia_caida == 0:
        dias_sin_lluvia += 1
    lluvia += lluvia_caida
print(f"Total de lluvia caída: {lluvia}")
print(f"Días que no llovió: {dias_sin_lluvia}")



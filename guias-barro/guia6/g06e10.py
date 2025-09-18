#10) Ingresar la lluvia caída en milímetros para cada día de la semana. 
# Mostrar al final el total de lluvia caída
# y el nombre del día que más llovió (sin repetir cantidades).

dic_semana = {}
dic_semana["Lunes"] = float(input('Ingrese la lluvia caída (en milímetros) del día Lunes: '))
dic_semana['Martes'] = float(input('Ingrese la lluvia caída (en milímetros) del día Martes: '))
dic_semana['Miercoles'] = float(input('Ingrese la lluvia caída (en milímetros) del día Miercoles: '))
dic_semana['Jueves'] = float(input('Ingrese la lluvia caída (en milímetros) del día Jueves: '))
dic_semana['Viernes'] = float(input('Ingrese la lluvia caída (en milímetros) del día Viernes: '))
dic_semana['Sábado'] = float(input('Ingrese la lluvia caída (en milímetros) del día Sábado: '))
dic_semana['Momingo'] = float(input('Ingrese la lluvia caída (en milímetros) del día Domingo: '))
print(dic_semana)

contador = 0
max_lluvia = 0
for k, v in dic_semana.items():
    if v > max_lluvia:
        max_lluvia = v
        dia_mas_llovio = k
    contador += v
print(f'El total de lluvia caída fue de {contador:.2f} milímetros.')
print(f'El día que mas llovió fue el {dia_mas_llovio}')
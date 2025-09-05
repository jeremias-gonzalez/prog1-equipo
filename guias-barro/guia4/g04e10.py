#10) Ingresar la lluvia caída en milímetros para cada día de la semana. 
#Mostrar al final el total de lluvia caída
#y el nombre del día que más llovió. 

lista_días = ['Lunes', 'Martes', "Miercoles", 'Jueves', 'Viernes', 'Sábado', 'Domingo']
Total = 0
max_lluvia = 0
for i in lista_días:
    lluvia_caída = float(input(f'Ingrese la cantidad de lluvia caída del {i}: '))
    if lluvia_caída > max_lluvia:
        max_lluvia += lluvia_caída
        día_mas_llovió = i
    Total += lluvia_caída
print(f'El día que más llovió fue: {día_mas_llovió}')
print(f'El total de lluvia caída de todos los días fue: {Total:.2f}')
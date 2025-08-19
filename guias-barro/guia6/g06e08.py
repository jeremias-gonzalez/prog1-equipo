#8) Dado el siguiente diccionario: notas = {"Juan": 85, "Ana": 92, "Luis": 78, "María": 95}, 
# crea una lista con los nombres de los estudiantes cuyas notas son mayores o iguales a 90.


diccionario_de_notas = {"Juan": 85, "Ana": 92, "Luis": 78, "María": 95}

lista_mas_90 = []
for k, v in diccionario_de_notas.items():
    if v > 90:
        lista_mas_90.append(k)
print(lista_mas_90)



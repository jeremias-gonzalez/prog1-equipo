# Pedir cuatro notas, calcular el promedio y mostrarlo.
#Salida ejemplo: El promedio de las notas 5, 7, 8 y 9 es 7.25 (como siempre, con los valores ingresados y el resultado verdadero)

nota1 = int(input("ingrese la primer nota: "))
nota2 = int(input("ingrese la segunda nota: "))
nota3 = int(input("ingrese la tercer nota: "))
nota4 = int(input("ingrese la cuarta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4
print(f"El promedio de las notas {nota1}, {nota2}, {nota3}, y {nota4} es {promedio}")
# 8) Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final.
# Se deberá ir preguntando si hay más números para ingresar.

maximo = 0
while True:
    numero = float(input("Ingrese números reales positivos: "))
    if numero < 0:
        print('¡Ese número es negativo!')
        break
    if numero > maximo:
        maximo = numero
    pregunta = str(input("Desea continuar? (si/no): "))
    if pregunta == "no":
        break
print(f"El número más alto que fue cargado es {maximo}")

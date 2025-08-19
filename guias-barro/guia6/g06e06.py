#6) Dado el siguiente diccionario: ventas = {"Enero": 5000, "Febrero": 6000, "Marzo": 4500}, 
# calcula el total de ventas sumando todos los valores del diccionario 
# y muestra el resultado.

ventas = {"Enero": 5000, "Febrero": 6000, "Marzo": 4500}
total = 0
for v in ventas.values():
    total += v
print(f"La suma del diccionario ventas que contienen a Enero, Febrero y Marzo es: {total}")


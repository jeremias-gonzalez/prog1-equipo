# 5) Preguntar cuántas personas se van a cargar 
personas = int(input("Cuantas personas desea cargar?: "))
suma_edades = 0
for i in range(personas):
    edades = int(input("ingrese la edad de cada persona: "))
    suma_edades += edades
promedio = suma_edades / personas
print(f"La edad promedio de las personas ingresadas son de: {promedio}")
#y luego solicitar sus edades, mostrando al final la edad promedio.
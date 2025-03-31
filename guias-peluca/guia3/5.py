cant = int (input ("Ingrese cuantas personas van a subirse: "))
tedad = int (0)
for x in range (cant):
    edad = int (input ("Ingrese la edad del pasajero: "))
    tedad = tedad + edad
    promedio = float (tedad / cant )
print (f"El promedio de edad es: {promedio}")    
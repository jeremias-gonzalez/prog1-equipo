#11) Cargar en listas los nombres y fechas de nacimiento de varias personas, 
#luego recorrerlo y mostrar los nombres de los mayores de edad.

Lista_nombres = ["Jorge", "Vargas", "Ramón", "Yanpiero", "Musculoso", "Alibaba"]
Listas_nacimientos = ["18/02/2005", "20/07/2004", "03/01/2002", "07/11/2008", "30/10/2010", "11/9/2011"]

año_actual = 2025
for i in range(len(Lista_nombres)):
    partes = Listas_nacimientos[i].split("/")

    año = int(partes[2])

    edad = año_actual - año

    if edad >= 18:
        print(f'{Lista_nombres[i]} es mayor a de edad ({edad} años)')
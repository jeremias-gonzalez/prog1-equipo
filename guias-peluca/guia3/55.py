cantpersonas = int (input ("Ingrese el numero de personas: ") )
tedad = 0
for x in range (cantpersonas):
    edad = int (input ("Cuantos años tiene: "))
    tedad = tedad + edad  
print (f" El promedio de edad de las personas es de {tedad / cantpersonas}")    
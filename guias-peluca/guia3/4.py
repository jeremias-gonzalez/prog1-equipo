gente = int (input ("Ingrese la cantidad de empleados: "))
total = 0
for x in range (gente):

    sueldo = int (input ("Ingrese su salario: "))
    total = total + sueldo
print (f"La suma de los montos es de ${total}" )    
#----------------PRACTICA 2 ---------------------


#1)
# numeroReal = float(input("ingresa un numero real:"))

# numeroReal = float(numeroReal)

# if numeroReal >= 0:
#     print('el numero  es real')
# elif numeroReal < 0 :
#     print(f'el numero real es {numeroReal} y es negativo')

#2)


# ingresaN1= int(input("ingresa un numero:"))
# ingresaN2 =int(input("ingresa otro para compararlos:"))

# ingresaN1=int(ingresaN1)
# ingresaN2 = int(ingresaN2)

# if ingresaN1 > ingresaN2:
#      print(f"el numero {ingresaN1} es mayor que el numero {ingresaN2}")
# elif ingresaN1 == ingresaN2 :
#      print("los valores ingresados son iguales")

#3)

#  Pedir el primer número
# pedir1 = int(input("Ingresa un número: "))

# # Pedir la opción de operación (+ o -)
# opcion = input("¿Quieres sumar (+) o restar (-)? ")

# # Pedir el segundo número
# pedir2 = int(input("Ingresa otro número: "))

# # Realizar la operación según la opción elegida
# if opcion == "sumar":
#     resultado = pedir1 + pedir2
#     print(f"La suma de {pedir1} y {pedir2} es igual a {resultado}.")
# elif opcion == "restar":
#     resultado = pedir1 - pedir2
#     print(f"La resta de {pedir1} y {pedir2} es igual a {resultado}.")
# else:
#     print("Opción no válida. Debes elegir '+' o '-'.")

#4)

# nombre = input("ingresa tu nombre:")
# edad= int(input("ingresa tu edad:"))

# nombre = (nombre)
# edad = int(edad)

# if edad == 18:
#     print(f"{nombre} tiene {edad}")
# elif edad > 18:
#     print(f"{nombre} es mayor a 18 y tiene {edad}")
# else:
#     print(f"{nombre} es menor que 18")

#5)

# ingresaUnNumero=int(input("ingresa un numero positivo de dos digitos"))

# ingresaUnNumero=int(ingresaUnNumero)

# if ingresaUnNumero > 9 and ingresaUnNumero < 100 :
#     print(f"el numero {ingresaUnNumero} es positivo y de dos digitos ")
# elif ingresaUnNumero < 0:
#     print(f"el numero {ingresaUnNumero} no es positivo de dos digitos")
# else:
#     print('fin')

#6)

# nombre = input("ingresa tu nombre:")
# localidad = input("vivis en rio cuarto?,si no es asi, de donde provenis?:")
# carrera = input("ingresa si tu carrera es mecatronica o turismo:")

# cuota=int(100000)

# if localidad == "rio cuarto":
#     print(f"el valor de la cuota es ${cuota}")
# elif localidad != "rio cuarto" and carrera == "mecatronica":
#     descuento = cuota * 0.15
#     resultado = float(cuota - descuento)
#     print(f'como cursas mecatronica y no sos de rio cuarto , el valor de la cuota es {resultado}')
# elif localidad != "rio cuarto" and carrera == "turismo":
#     descuento = cuota * 0.05
#     resultado = float(cuota - descuento)
#     print(f'como cursas turismo y no sos de rio cuarto , el valor de la cuota es {resultado}')

#7)

# nombre = input("ingrese su nombre")

# edad = int(input("ingrese su edad"))

# edad=int(edad)

# pasaje=int(20000)

# if edad >= 5 and edad <=10:
#     descuento = pasaje* 0.4
#     resultado = float(pasaje - descuento)
#     print(f"{nombre} de {edad} tiene un costo de pasaje de {resultado}")
# elif edad >= 65:
#     descuento = pasaje* 0.4
#     resultado = float(pasaje - descuento)
#     print(f"{nombre} es jubilado y tiene un costo de pasaje de {resultado}")
# else:
#     print(f"el pasaje vale {pasaje}")

#8)


nombre = input("ingresa tu nombre:")
diasNoTrabajados = int(input("cantidad de dias no trabajados:"))
añoDeIngreso= int(input("ingresa tu año de ingreso a la empresa:"))

añoDeIngreso=int(añoDeIngreso)
diasNoTrabajados = int(diasNoTrabajados)
diasDelAño=int(365)
sueldoBasico=int(1000000)
añoActual=int(diasDelAño == 2025)
antiguedad= int(diasDelAño * 5)


if diasNoTrabajados == 0 and añoDeIngreso < añoActual:
    adicicional= sueldoBasico * 0.30
    resultado = int(sueldoBasico + adicicional)
    print(f"{nombre}:Ausentismo = {diasNoTrabajados}/ Año de ingreso = {añoDeIngreso} /sueldo:{resultado}")
elif diasNoTrabajados == 0 and antiguedad < añoActual:
      print(f"{nombre}:Ausentismo = {diasNoTrabajados}/ Año de ingreso = {añoDeIngreso} / sueldo:{sueldoBasico}")

else:
     print('nada')
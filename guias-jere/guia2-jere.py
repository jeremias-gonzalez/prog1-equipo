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

#  # Pedir la opción de operación (+ o -)
# opcion = input("¿Quieres sumar (+) o restar (-)? ")

#  # Pedir el segundo número
# pedir2 = int(input("Ingresa otro número: "))

# # # Realizar la operación según la opción elegida
# if opcion == "sumar":
#       resultado = pedir1 + pedir2
#       print(f"La suma de {pedir1} y {pedir2} es igual a {resultado}.")
# elif opcion == "restar":
#        resultado = pedir1 - pedir2
#        print(f"La resta de {pedir1} y {pedir2} es igual a {resultado}.")
# else:
#      print("Opción no válida. Debes elegir '+' o '-'.")

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


# Entrada de datos
# nombre = input("Ingresa tu nombre: ")
# diasNoTrabajados = int(input("Cantidad de días no trabajados: "))
# añoDeIngreso = int(input("Ingresa tu año de ingreso a la empresa: "))

# # Definición de constantes
# añoActual = 2025
# sueldoBasico = 1000000

# # Cálculo de antigüedad en años
# antiguedad = añoActual - añoDeIngreso

# # Cálculo del sueldo según condiciones
# if diasNoTrabajados == 0 and antiguedad >= 5:
#     adicional = sueldoBasico * 0.30  # 30% adicional
#     sueldoFinal = sueldoBasico + adicional
#     print(f"{nombre}: Ausentismo = {diasNoTrabajados} / Año de ingreso = {añoDeIngreso} / Sueldo: {sueldoFinal}")
# elif diasNoTrabajados == 0:
#     print(f"{nombre}: Ausentismo = {diasNoTrabajados} / Año de ingreso = {añoDeIngreso} / Sueldo: {sueldoBasico}")
# else:
#     print(f"{nombre}: No cumple condiciones para bono. Sueldo: {sueldoBasico}")
 
#9)
# peso = input("ingrese su peso:")
# altura = input("ingrese su altura:")

# peso=float(peso)
# altura=float(altura)

# formula = peso/altura**2

# if formula < 18.5:
#     print("bajo peso")
# elif formula > 18.5 and formula <=24.9:
#     print("su peso es normal")
# elif formula > 25 and formula <=29.9:
#     print("sobrepeso")
# elif formula >= 30:
#     print("sos una heladerovich anaannnshei")

# print(f"su indice de masa corporal es de:{formula}")

# pesoPaquete= int(input("ingresa el peso del packete en kg:"))
# distancia=int(input("ingrese la distancia en km:"))

# pesoPaquete=int(pesoPaquete)
# distancia=int(distancia)
# if pesoPaquete > 0 and pesoPaquete < 2:
#     base = 150
#     total = base + 10 * distancia
#     print(f"El costo total de envío de tu paquete de {pesoPaquete} kg a una distancia de {distancia} km es de ${total}")
# elif pesoPaquete > 0 and pesoPaquete < 6:
#     base = 300
#     total = base + 20 * distancia
#     print(f"El costo total de envío de tu paquete de {pesoPaquete} kg a una distancia de {distancia} km es de ${total}")
# elif pesoPaquete > 4 and pesoPaquete < 11:
#     base = 450
#     total = base + 30 * distancia
#     print(f"El costo total de envío de tu paquete de {pesoPaquete} kg a una distancia de {distancia} km es de ${total}")
# elif pesoPaquete > 10:
#     print("No enviamos paquetes de 10 kg o más")
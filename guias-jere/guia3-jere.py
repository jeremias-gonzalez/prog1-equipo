#1)

# numero = int(input('ingrese un numero'))

# for numero in range (0,10):
#     numero = numero + 1
#     print(numero)

#2)
# contador=0
# for numeroIngresado in range(1,6):
#     numeroIngresado= int(input("ingresa un numero:"))
#     if numeroIngresado > 23:
#        contador = contador +1


# print(f"los numeros mayores a 23 son {contador}")

#3)

# for numerosN in range(0,-9,-1):
#     print(numerosN)

#4)

# seguirIngresando = "si"
# total = 0
# while seguirIngresando == "si":
#     ingresaSueldos = int(input("ingresa un sueldo:"))
#     print(f"sueldo ingresado{ingresaSueldos}")
#     ingresaSueldos = ingresaSueldos
#     seguirIngresando = input("Quieres seguir ingresando sueldos? si/no:")
#     total = total + ingresaSueldos
# print(f"el total de sueldos ingresados es de:{total}")

#5)
#VERSION CHAT GPT Y YO.
# pregunta = "si"
# totalEdades = 0
# cantidadPersonas = 0

# while pregunta == "si":
#     personas = int(input("¿Cuántas personas se van a cargar?: "))
#     print(f"Genial, entonces son {personas} personas")


#     for i in range(personas):
#         edad = int(input(f"Ingresa la edad de la persona {i+1}: "))
#         totalEdades = totalEdades + edad
#         cantidadPersonas = cantidadPersonas + 1


#     pregunta = input("¿Vas a seguir cargando personas? (si/no): ")


# if cantidadPersonas > 0:
#     promedio = int( totalEdades / cantidadPersonas)
#     print(f"La edad promedio es: {promedio}")
# else:
#     print("No se han ingresado edades.")

#6)
# i = 5
# for i in range (1,65):
#     if i % 5 == 0:
#         print(f"{i} es multiplo de 5")

#7)
# pregunta ="si"
# contador = 0
# while pregunta == "si":
#       auto = str (input ("Ingrese el auto: "))
#       precio = int (input ("Ingrese el precio: "))
#       if precio >= 27460000 and precio <= 33850000:
#           contador = contador + 1


#       pregunta=input("Queres seguir? Si / No ")

#8)
# pregunta = "si"

# nMax = float(0)

# while pregunta  == "si":
#      nMin = float(input("ingresa un numero real positivo: "))
#      if nMin > nMax:
#         nMax = nMin
#      pregunta = input("Hay mas numeros para ingresar? Si / No:")

# print(f'el numero mayor ingresado es {nMax}')


#9)


# pregunta = 's'
# nMin = float('inf')  
# nombreMin = str
# while pregunta == 's':
#     nombre = input("Ingresa un nombre: ")
#     salario = int(input('Ingresa su salario: '))
    
#     if salario  < nMin:  
#         nMin = salario
#         nombreMin = nombre
#     pregunta = input('¿Quieres seguir operando? (s/n): ')

# print(f"El salario menor es {nMin} y correspomde a {nombreMin}") 


#10)

# numero = int(input("Ingrese 7 numeros:"))
# repetir = numero
# cartel = 0
# for repetir in range (1,7):
#     repetir = int(input(f"ingrese otro:"))
#     if repetir < 10 :
#         cartel = repetir
        
        

# print(f"{cartel}")

#11)
# nombre = ""
# sexo = ""
# totalMujeres = 0
# totalNombres = ""
# pregunta = "s"

# while pregunta == "s":
#     nombre = input("Ingrese nombre:")
#     sexo = input("Ingrese Sexo:")
#     pregunta = input("vas a seguir ingresando personas? s/n:")
#     if sexo == "fem":
#         totalMujeres = totalMujeres +1
#         totalNombres = totalNombres +","+ nombre

# print(f"El total de mujeres ingresado es : {totalMujeres}")
# print(f"Sus nombres son : {totalNombres}")

#12)

# lluvia = 0 
# dias = 0
# totalLluvia = 0
# totalDias= 0
# for lluvia in range (1,8):
#     dias = dias + 1
#     lluvia = int(input(f"ingresa mas milimitetros para el dia {dias}: "))
#     if lluvia > 0:
#         totalLluvia = totalLluvia + lluvia
#     elif lluvia == 0 :
#         totalDias = totalDias + 1
    
    
# print(f"El total que llovido en mm de la semana es {totalLluvia}")
# print(f"El total de dias que no llovio son : {totalDias}")
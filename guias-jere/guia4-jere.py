#1)
# listNum=[]
# contador =0
# for num in range (10):
#     num = int(input("Ingrese un numero:"))
#     if num > 23 :
#         contador  = contador +1
#         listNum.append(num)

# print(f"Los numeros son {listNum} y la cantidad es {contador}")

#2)
#Cargar letras en una lista hasta que el usuario ingrese un asterisco
#Luego hacer otra iteración para contar las vocales. Al final mostrar el total.
# letras =[]
# pregunta = "s"
# totalVocales = ["a","e","i","o","u"]
# contador=0
# otralista= []
# while pregunta == "s":
#  letra = input("carga una letra: ")
#  letras.append (letra)
#  pregunta = input("Si no quieres seguir ingresando letras presiona * sino s: ")
# for letrita in letras:
#       if letrita in totalVocales :
#           otralista.append(letrita)
#           contador = contador + 1
         
# print(f"el total de vocales ingresadas son {contador} y {otralista}")

#3)
# names = []
# sex = []
# otherList= []
# question = "s"
# contador=0
# otherSecondList= []


# while question == "s":
#     nm = input("ingresa un nombre:")
#     sx = input("ingresa el sexo:")
#     names.append(nm)
#     sex.append(sx)
#     question = input("quieres seguir ingresando:")

#     for i in range(len(names)):
#         personas = (names[i],sex[i])
#         otherList.append(personas)

#     for i in range(len(otherList)):
#         girls = otherList[i]
#         for i in range(len(girls)):
#             if girls[i] == "f":
#                 otherSecondList.append(girls)
#                 contador= contador+1

    
# print(otherSecondList)
# print(contador)
        
#4)
# listaN=[2,4,6]
# listaCuadrada=[]

# for i in listaN:
#     if i in listaN :
#         resultado= i**2
#         listaCuadrada.append(resultado)
# print(listaCuadrada)

#5)
# numeros=0
# pregunta="s"
# listaPares=[]

# while pregunta == "s":
#      numeros = int(input("ingresa los numeros pares que quieras:"))
    
#      if numeros > 0 and numeros < 31:
#         listaPares.append(numeros)
#      pregunta=input("quieres seguir agregando numeros:")

# print(listaPares)

#6)
# nombres=[]
# nombre=""
# hayMas= 'si'
# buscar=""
# while hayMas == 'si':
#     nombre+input('ingresa un nombre:')
#     nombres.append(nombre)
#     hayMas=input('hay mas?:')
#     buscar = input('Busca un nombre y sabras su posicion la posicion:')
# for nombre in nombres:
#         print(f'su posicion es {nombres.index(nombre)}')

# if nombre in nombres:
#      print(f'esta repetido ingrese otro y se encuentra en la posicion:{nombres.index(nombre)} ')





# Ingresar nombres en una lista sin repetir, 
# luego buscar un nombre y de encontrarlo decir en qué posición está.
lisNombres = []
pregunta = "s"

while pregunta == "s":
    nombre = input("Ingresa un nombre: ")
    if nombre not in lisNombres:
        lisNombres.append(nombre)
    else:
        print(f"'{nombre}' ya existe en la lista. No se agregará de nuevo.")
    pregunta = input("¿Deseas ingresar otro nombre? (s/n): ")

buscar = input("\nIngresa el nombre que deseas buscar: ")
if buscar in lisNombres:
    indice = lisNombres.index(buscar)
    print(f"'{buscar}' se encuentra en la posición {indice + 1} de la lista.")
else:
    print(f"'{buscar}' no se encuentra en la lista.")


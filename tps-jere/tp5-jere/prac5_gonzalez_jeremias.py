
with open("tps-jere/tp5-jere/clientes.txt") as clientes:
    # Guardar cada línea en una lista, quitando saltos de línea
     lineas = clientes.readlines()

localidades=[]
lista=[]
for i in range(len(lineas)):
    lineas[i] = lineas[i].strip()
    lista.append(lineas[i].split("#"))
# print(lista)

def apellidos():
      lista_apellidos=[]
      lista_dni=[]
     
      lista_conjunta=[]
      for i in lista:
          lista_dni.append(i[0])
          lista_conjunta.append((i[0],i[1].split(" ")[1]))
          salida = lista_conjunta
          if i[0] and i[1] in salida :
               dni = int(i[0])
               if dni > 40000000:
                 lista_apellidos.append(i[1])

      return lista_apellidos
print(apellidos())

#---------------1)--------------------        
# for i in lineas:
#     localidades.append(i.split("#")[3])
# print(localidades)
# def cantidadPersonas (localidades):
#     contador = 0
#     ingresarLocalidad=input("ingresa una localidad para saber la cantidad de personas: ")
#     if ingresarLocalidad in localidades:
#                for localidad in localidades:
#                    if ingresarLocalidad == localidad:
#                           contador += 1
#                return print(f"La cantidad de clientes en {ingresarLocalidad} es {contador}")

# print(cantidadPersonas(localidades))

#-----------------------------2)-------------------------------------------
# def deudaAcumulada1():
#     total = 0
    
#     for i in lista:
#         posicion = int(i[2])
#         if posicion > 90000:
#             total += posicion
           
#     return print(f"El total de deuda acumulada de los clientes que deben más de 90.000 pesos es {total} ")

# deudaAcumulada1()

# def deudaAcumulada2():
#     total = 0
   
#     for i in lista:
#         posicion = int(i[2])
#         if posicion < 40000:
#             total += posicion
          
#     return print(f"El total de deuda acumulada de los clientes que deben más de 40.000 pesos es {total} ")

# deudaAcumulada2()
#-----------------------------3)------------------------------


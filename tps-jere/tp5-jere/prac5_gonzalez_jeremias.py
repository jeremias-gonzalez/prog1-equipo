
with open("tps-jere/tp5-jere/clientes.txt") as clientes:
    # Guardar cada línea en una lista, quitando saltos de línea
     lineas = clientes.readlines()

localidades=[]
lista=[]
for i in range(len(lineas)):
    lineas[i] = lineas[i].strip()
    print(lineas[i])

# for i in lineas:
#     localidades.append(i.split("#")[3])
# print(localidades)
# def cantidadPersonas (localidades):
#      contador = 0
#      acumulador= 0
#      for x in localidades:
#             if x == "La Carlota":
#              pass
#              contador += 1
#      print(f"La cantidad de clientes de La Carlota es: {contador}")
#      ingresarLocalidad=input("ingresa una localidad para saber la cantidad de personas: ")
#      if ingresarLocalidad in localidades:
#                 for localidad in localidades:
#                     if ingresarLocalidad == localidad:
#                            acumulador += 1
#                 return print(f"La cantidad de clientes en {ingresarLocalidad} es {acumulador}")

# print(cantidadPersonas(localidades))

def deudaAcumulada():
    total = 0
    monto=input(int("Ingresa un monto:"))

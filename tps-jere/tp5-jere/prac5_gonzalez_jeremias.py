
with open("tps-jere/tp5-jere/clientes.txt") as f:
    # Guardar cada línea en una lista, quitando saltos de línea
     lineas = f.readlines()

localidades=[]
        
for i in range(len(lineas)):
    lineas[i] = lineas[i].strip()
    print(lineas[i])

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

def deudaAcumulada():
    total = 0
    monto=input(int("Ingresa un monto:"))

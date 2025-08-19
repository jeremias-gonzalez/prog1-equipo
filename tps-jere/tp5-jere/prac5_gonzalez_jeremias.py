
with open("tps-jere/tp5-jere/clientes.txt") as f:
    # Guardar cada línea en una lista, quitando saltos de línea
     lineas = f.readlines()

localidades=[]

def cantidadPersonas ():
    contador = 0
    #ingresarLocalidad=input("ingresa una localidad para saber la cantidad de personas: ")
    for linea in lineas:
        partes = linea.split("#")
        localidades.append(partes[3])
        localidades.remove("\n")
    mensaje = print(localidades)
    
     
    # if ingresarLocalidad in localidades:
    #          for localidad in localidades:
    #              if ingresarLocalidad == localidad:
    #               contador += 1

    #          mensaje = print(f"La cantidad de clientes en {ingresarLocalidad} es {contador}")
                

    return mensaje

print(cantidadPersonas())
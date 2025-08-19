
with open("/workspaces/prog1-equipo/tps-jere/tp5-jere/clientes.txt", encoding="utf-8") as f:
    # Guardar cada línea en una lista, quitando saltos de línea
     lineas = f.readlines()

def cantidadPersonas ():
    contador = 0
    ingresarLocalidad=input("ingresa una localidad para saber la cantidad de personas:")
    for linea in lineas:
        partes = linea.split("#")
        nuevaLista = partes
        localidades = nuevaLista[3]
        # mensaje=print()
        pass
    if ingresarLocalidad in localidades:
             for localidad in localidades:
                 if ingresarLocalidad == localidad:
                  contador += 1

                 mensaje = print(f"La cantidad de clientes en {ingresarLocalidad} es {contador}")
    else:
        print("Opción inválida")

    return mensaje

print(cantidadPersonas())
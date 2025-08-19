#Tengo un archivo clientes.txt con los siguientes datos de clientes:
#DNI, nombre y apellido, monto de deuda en pesos y localidad. Quiero obtener:
#1) La cantidad de clientes de ... (localidad literal y variable)

buscar_localidad = input("Ingrese una localidad: ")

contador = 0

with open('clientes.txt', 'r') as archivo:
    next(archivo)  # Saltar la primera línea (encabezado)
    for linea in archivo:
        datos = linea.strip().split('#')
        localidad = datos[3]
        if localidad == buscar_localidad:
            contador += 1

print(f"La cantidad de clientes de {buscar_localidad} es {contador}.")


#2)
limite_del_monto = float(input("Ingrese el monto límite de deuda: "))
opcion = input("¿Desea ver los que deben más o menos que ese monto? (mas/menos): ")

total_deuda = 0

with open('clientes.txt', 'r') as archivo:
    next(archivo)  # Saltar encabezado
    for linea in archivo:
        datos = linea.strip().split('#')
        deuda = float(datos[2])
        
        if opcion == "mas" and deuda > limite_del_monto:
            total_deuda += deuda
        elif opcion == "menos" and deuda < limite_del_monto:
            total_deuda += deuda

print(f"El total de deuda acumulada de los clientes que deben {opcion} de {limite_del_monto} pesos es ${int(total_deuda)}")



#3)

dni_limite = int(input("Ingrese un número de DNI como límite inferior: "))

with open('clientes.txt', 'r') as archivo, open('apellidos.txt', 'w', 'r') as salida:
    next(archivo)  # Saltar encabezado
    salida(f"Apellidos de los clientes con DNI mayor a {dni_limite}\n")

    for linea in archivo:
        datos = linea.strip().split('#')
        dni = int(datos[0])
        nombre_apellido = datos[1]

        if dni > dni_limite:
            apellido = nombre_apellido.split()[-1]  # Toma el último nombre como apellido
            salida.write(f"{apellido}\n")

print("Archivo 'apellidos.txt' creado con éxito.")

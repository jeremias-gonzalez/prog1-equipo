personas = []
with open ('tps-peluca/tp5-peluca/clientes.txt', 'r', encoding="utf-8") as archivo:
    next(archivo)  # Con esto salto la primera linea de la lista ('DNI,nombre y apellido,monto de deuda en pesos,localidad')
    for linea in archivo:
        dni, nombre, deuda, localidad = linea.strip().split('#')
        personas.append((dni, nombre, deuda, localidad))


'''
# 1) La cantidad de clientes de ... (localidad literal y variable)
def cantidad_clientes(localidad):
    contador = 0
    for persona in personas:
        if persona[3] == localidad:
            contador += 1
    return contador

print (f"La cantidad de clientes en la localidad especificada es: {cantidad_clientes('Villa María')}")


def cantidad_clientes(localidad):
    contador = 0
    for persona in personas:
        if persona[3] == localidad:
            contador += 1
    return contador

buscador = input("Ingrese la localidad: ")
print (f"La cantidad de clientes en la localidad especificada es: {cantidad_clientes(buscador)}")


# 2) El total de deuda acumulada de los clientes que deben ... (mas o menos que)
def deuda_acumulada_mayor(monto1):
    
    total = 0
    
    for persona in personas:
        deuda = int(persona[2])
        if deuda > monto1:
            total += deuda
    return total


def deuda_acumulada_menor(monto2):
    
    total = 0
    
    for persona in personas:
        deuda = int(persona[2])
        if deuda < monto2:
            total += deuda
    return total
pregunta_mayor = input('Ingrese el monto que deban mas de: ')
pregunta_menor = input('Ingrese el monto que deban menos de: ')


deuda_acumulada_mayor(int(pregunta_mayor))
deuda_acumulada_menor(int(pregunta_menor))

print(f"La deuda acumulada de los clientes que deben mas de {pregunta_mayor} es: {deuda_acumulada_mayor(int(pregunta_mayor))}")
print(f"La deuda acumulada de los clientes que deben menos de {pregunta_menor} es: {deuda_acumulada_menor(int(pregunta_menor))}")

# 3) Los apellidos de los clientes cuyos DNI sean mayores a ... (esta salida DEBE grabarse en un archivo llamado apellidos.txt) 
'''
def apellidos_mayores_a(dni):
    apellidos = []
    for persona in personas:
        if int(persona[0]) > dni:
            apellido = apellidos.append(persona[1].split()[-1])
    
    with open('tps-peluca/tp5-peluca/apellidos.txt', 'w', encoding='utf-8') as archivo:
        for apellido in apellidos:
            archivo.write(apellido + '\n')
 
    return print('Se subieron correctamente los apellidos.')


apellidos_mayores_a(30000000)
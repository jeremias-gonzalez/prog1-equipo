personas = []
with open ('tps-peluca/tp5-peluca/clientes.txt', 'r', encoding="utf-8") as archivo:
    next(archivo)  # Con esto salto la primera linea de la lista ('DNI,nombre y apellido,monto de deuda en pesos,localidad')
    for linea in archivo:
        dni, nombre, deuda, localidad = linea.strip().split('#')
        personas.append((dni, nombre, deuda, localidad))

print (personas)

# 1) La cantidad de clientes de ... (localidad literal y variable)
def cantidad_clientes(localidad):
    contador = 0
    for persona in personas:
        if persona[3] == localidad:
            contador += 1
    return contador

print (f"La cantidad de clientes en la localidad especificada es: {cantidad_clientes('Villa María')}")
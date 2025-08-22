personas = []
with open ('tps-peluca/tp5-peluca/clientes.txt', 'r', encoding="utf-8") as archivo:
    for linea in archivo:
        personas.append(linea.strip())

print (personas)
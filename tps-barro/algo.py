rank_bebes2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
rank_bebes2018 = "Liam,19837,m,Emma,18688,f,Noah,18267,m,Olivia,17921,f,Michael,14516,m,Ava,14924,f,James,13525,m,Isabella,14464,f,Oliver,13389,m,Sophia,13928,f"

listahombres2018 = []
listahombres2008 = []

listamujeres2018 = []
listamujeres2008 = []

lista2008 = []
lista2018 = []
lisranking2018 = rank_bebes2018.split(",")
lisranking2008 = rank_bebes2008.split(",")
#Acá lo que hago es ir agrupando los nombres del 2018

for x in range (len(lisranking2018)):
    if x % 3 == 0:  
        nombre = lisranking2018 [x]
        cantidad = lisranking2018 [x + 1]
        sexo = lisranking2018 [x + 2]
 
        lista2018.append((nombre, cantidad, sexo)) 


#Acá lo que hago es ir agrupando los nombres del 2008
for x in range (len(lisranking2008)):
    if x % 3 == 0:  
       
        nombre = lisranking2008 [x]
        cantidad = lisranking2008 [x + 1]
        sexo = lisranking2008 [x + 2]
 
        lista2008.append((nombre, cantidad, sexo)) 


#Acá lo que hago es ordenar de menor a mayor la lista del 2008
for x in range (len(lista2008)):
    nombre,cantidad,sexo = lista2008[x]
    lista2008[x] = (int(cantidad), nombre,sexo)

#Con esto, lo que hago es que se acomode de mayor a menor
lista2008.sort(reverse=True)

for x in range (len(lista2008)):
    cantidad,nombre,sexo = lista2008[x]
    lista2008[x] = (nombre,cantidad,sexo)




#Acá lo que hago es ordenar de menor a mayor la lista del 2018
for x in range (len(lista2018)):
    nombre,cantidad,sexo = lista2018[x]
    lista2018[x] = (int(cantidad), nombre,sexo)

#Con esto, lo que hago es que se acomode de mayor a menor 
lista2018.sort(reverse=True)

for x in range (len(lista2018)):
    cantidad,nombre,sexo = lista2018[x]
    lista2018[x] = (nombre,cantidad,sexo)

#Acá lo que hago e separar los nombres que sean de hombres del 2018
for x in lista2018:
    nombre, cantidad, sexo = x 
     
    if  sexo == "m":
        
        listahombres2018.append(x)


#Acá lo que hago e separar los nombres que sean de hombres del 2008
for x in lista2008:
    nombre, cantidad, sexo = x 
     
    if  sexo == "m":
        
        listahombres2008.append(x)

#Acá lo que hago e separar los nombres que sean de mujeres del 2018
for x in lista2018:
    nombre, cantidad, sexo = x 
     
    if  sexo == "f":
        
        listamujeres2018.append(x)

for x in lista2008:
    nombre, cantidad, sexo = x 
     
    if  sexo == "f":
        
        listamujeres2008.append(x)
        



print (listahombres2008)
print (listahombres2018)
print (listamujeres2008)
print (listamujeres2018)

# 1- La diferencia en cantidad de bebés que existe entre los nombres de misma posición y mismo sexo. Se solicita posición y sexo. 
#Esto es para los hombres
for x in range  (len(listahombres2008)):
    ranking = x +1
    if listahombres2008[x][1] > listahombres2018 [x][1]:
        resultado = listahombres2008[x][1] - listahombres2018 [x][1]
        print (f"Hombres en el top #{ranking}: {resultado} es la diferencia entre, {listahombres2008[x][0]} del 2008 sobre {listahombres2018[x][0]} del 2018")
    else:
        resultado = listahombres2018[x][1] - listahombres2008 [x][1]        
        print (f"Hombres en el top #{ranking}: {resultado} es la diferencia entre, {listahombres2018[x][0]} del 2018 sobre {listahombres2008[x][0]} del 2008")
#Esto es para las mujeres
for x in range  (len(listamujeres2008)):
    ranking = x +1
    if listamujeres2008[x][1] > listamujeres2018 [x][1]:
        resultado = listamujeres2008[x][1] - listamujeres2018 [x][1]
        print (f"Mujeres en el top #{ranking}: {resultado} es la diferencia entre, {listamujeres2008[x][0]} del 2008 sobre {listamujeres2018[x][0]} del 2018")
    else:
        resultado = listamujeres2018[x][1] - listamujeres2008 [x][1]        
        print (f"Mujeres en el top #{ranking}: {resultado} es la diferencia entre, {listamujeres2018[x][0]} del 2018 sobre {listamujeres2008[x][0]} del 2008")


#Ingresar una letra y buscar los nombres que empiecen por la misma 

buscador = input ("Ingresa la letra que quieres buscar: ")

nombres_encontrados = []

for nombre in lista2018:
    if nombre[0][0] == buscador:  
        nombres_encontrados.append(nombre[0])
    

for nombre in lista2008:
    if nombre[0][0] == buscador:  
        nombres_encontrados.append(nombre[0])

final = ", ".join(nombres_encontrados)
print(final)


#Encontrar los nombres repetidos en todas las listas
nombres_repetidos = []

for x2018 in lista2018:
    nombre2018 = x2018[0]
    for x2008 in lista2008:
        nombre2008 = x2008[0]
        if nombre2018 == nombre2008 and nombre2018 not in nombres_repetidos:
            nombres_repetidos.append(nombre2018)


nombres = ", ".join(nombres_repetidos)
print (nombres)

#concatenar:
# concatenación
una_cadena = "primera cadena"
otra_cadena = "segunda cadena"
nueva_cadena = una_cadena + " - " + otra_cadena
print(nueva_cadena)

#Recorrer como una lista:
nombre = "Juan" # recorremos como si fuera esta lista: ['J', 'u', 'a', 'n']
for i in range(len(nombre)): # por índice
    print(nombre[i])

for letra in nombre: # lo mismo pero por elemento
    print(letra)

#A diferencia de las listas son inmutables:
lista = ['m', 'e', 's', 'a']
cadena = "mesa" 
lista[1] = 'i' # Funciona
cadena[1] = 'i' # NO funciona, no se puede modificar parcialmente


frase = "Las noches de otoño son frescas"
posicion = frase.find("otoño")  # busca subcadena y devuelve posición
print(posicion)
otra_posicion = frase.find("s no")  # no tiene que ser una palabra
print(otra_posicion)
no_existe = frase.find("no s")  # -1 si no existe
print(no_existe)
print(frase.find("es"))  # encuentra el "es" de "noches"
print(frase.find("es", 10))  # encuentra "es" en "frescas" (por qué?)

#Split (Convertir a lista)
#Separar una cadena con split:
fecha = "3/5/2022"
lista_fecha = fecha.split("/")
print(lista_fecha)  # ['3', '5', '2022']

nombres = "juan---ana---pedro---luisa"
print(nombres.split("---"))  # ['juan', 'ana', 'pedro', 'luisa']

cadena = "algo otro cosa techo"
print(cadena.split()) # por defecto separa por espacio en blanco

# Una operación muy utilizada (aplica también a listas)
frase = "Las noches de otoño son frescas"
print(frase[4:10])  # noches
comienzo = frase[:3]
print(comienzo)  # Las
final = frase[-7:]
final2 = frase[24:]
print(final, final2)  # frescas
print(frase[-1])
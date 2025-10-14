#Los siguientes ejercicios son en su mayoría para reutilizar los enunciados de guías anteriores, aplicando en la solución el uso de funciones.
#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, 
#considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#2) Buscar una palabra y reemplazarla por otra todas las veces que aparezca. 
#Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'

texto = "Quiero comer manzanas, solamente manzanas."

coma = texto.replace(",", "")
punto = coma.replace(".", "")
separar = punto.split(" ")
reemplazar = input('¿Palabra que quiera reemplazar?: ')
palabra = input('¿Palabra que quiere incluir?: ')
def reemplazo(lista, palabra_nueva, palabra_vieja):
    for i in range(len(lista)):
        if lista[i] == palabra_vieja:
            lista[i] = palabra_nueva
    if lista[i] not in palabra_vieja:
        print("Esa palabra no está en la lista")
reemplazo(separar, reemplazar, palabra)
juntar = " ".join(separar)
print(juntar)


#Los siguientes ejercicios son en su mayoría para reutilizar los enunciados de guías anteriores, aplicando en la solución el uso de funciones.
#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, 
#considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#3) Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes). El resultado es el total general.

texto = "Quiero comer manzanas, solamente manzanas."

def total(cantidad):
    contador = 0
    for i in cantidad:
        contador += 1
    return contador
resultado = total(texto)
print("El total es", resultado)


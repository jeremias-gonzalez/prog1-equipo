#Los siguientes ejercicios son en su mayoría para reutilizar los enunciados de guías anteriores, aplicando en la solución el uso de funciones.
#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, 
#considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#4) Contar la cantidad de palabras.

texto = "Quiero comer manzanas, solamente manzanas."
lista_frase = texto.split(' ')
def palabras(contar):
    print(f'El texto cuenta con {len(contar)} palabras')

palabras(lista_frase)
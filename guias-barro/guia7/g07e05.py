#Los siguientes ejercicios son en su mayoría para reutilizar los enunciados de guías anteriores, aplicando en la solución el uso de funciones.
#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, 
#considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#5) Averiguar qué cantidad de letras tiene la palabra más larga. 
#Para ello, primero cargar cada palabra en una lista y luego obtener la solicitada.
#Usar dos funciones.
texto = "Quiero comer manzanas, solamente manzanas."
def obtener_palabras():
    coma = texto.replace(",", "")
    punto = coma.replace(".", "")   
    separar = punto.split(" ")

def palabra():
    palabras = []
    long_palabras = 0
    for i in separar:
        if len(i) > long_palabras:
            long_palabras = len(i)
            palabras = i
    print(f'La palabra mas larga es {palabras} y tiene {long_palabras} letras')

#Los siguientes ejercicios son en su mayoría para reutilizar los enunciados de guías anteriores, aplicando en la solución el uso de funciones.
#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, 
#considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#1) Cuántas veces se repite una letra cualquiera. Parámetros: letra, cadena.
texto = "Quiero comer manzanas, solamente manzanas."
ingresar_letra = input("Ingrese una letra: ")
def contar_letras(letra, cadena):
    contador = 0
    for i in range(len(cadena)):
        if letra == cadena[i]:
            contador += 1
    print(f"La letra {letra} se repite: {contador} veces")

contar_letras(ingresar_letra, texto)

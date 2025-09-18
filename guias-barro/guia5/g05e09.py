#9) En los siguientes ejercicios (del 4 al 9) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”.
#Considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#9) Mostrar qué cantidad de letras tiene la palabra más larga y cual es.

frase = "Quiero comer manzanas, solamente manzanas."
coma = frase.replace(",", "")
punto = coma.replace(".", "")
separar = punto.split(" ")


palabras = ""
long_palabras = 0
for i in separar:
    if len(i) > long_palabras:
        long_palabras = len(i)
        palabras = i
print(f'La palabra mas larga es {palabras} y tiene {long_palabras} letras')

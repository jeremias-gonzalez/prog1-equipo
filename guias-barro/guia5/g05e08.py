#8) En los siguientes ejercicios (del 4 al 9) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”.
#Considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#8) Determinar cuál es la vocal que aparece con mayor frecuencia.

frase = "Quiero comer manzanas, solamente manzanas."
lista_vocales = ["a", "e", "i", "o", "u"]
lista_frase = frase.split(" ")
juntar = " ".join(lista_frase)

for vocal in lista_vocales:
    contador = 0
    for letra in frase:
        if letra == vocal:
            contador += 1
    print(f'La vocal {vocal} aparece {contador} veces')
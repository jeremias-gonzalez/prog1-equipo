#7) En los siguientes ejercicios (del 4 al 9) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”.
#Considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#7) Contar la cantidad de palabras.

frase = "Quiero comer manzanas, solamente manzanas."
lista_frase = frase.split(' ')
print(f'El texto cuenta con {len(lista_frase)} palabras')
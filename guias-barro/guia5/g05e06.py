#6) En los siguientes ejercicios (del 4 al 9) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”.
#Considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#6) Contar la cantidad de letras (no incluir los separadores).

frase = "Quiero comer manzanas, solamente manzanas."
coma = frase.replace(",", "")
punto = coma.replace(".", "")
split = punto.split(" ")
juntar = "".join(split)

contador = 0
for i in juntar:
    contador += 1
print(f'El texto tiene {contador}')

#5) En los siguientes ejercicios (del 4 al 9) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”.
#Considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#5) Buscar una palabra y reemplazarla por otra todas las veces que aparezca. 
# Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.' Sin usar replace.

texto = 'Quiero comer manzanas, solamente manzanas.'
coma = texto.replace(",", "")
punto = coma.replace(".", "")
split = punto.split(" ")
reemplazo = input('¿Palabra que quiera reemplazar?: ')
for i in range(len(split)):
    if reemplazo == split[i]:
        split[i] = "peras"
juntar = " ".join(split)
print(juntar)
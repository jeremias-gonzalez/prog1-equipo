#En los siguientes ejercicios (del 4 al 9) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”.
#Considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#4) Buscar una palabra completa en un texto y contar cuántas veces está.
texto = "Quiero comer manzanas, solamente manzanas"
reemplazo_coma = texto.replace(",", "")
reemplazo_punto = reemplazo_coma.replace(".", "")
separar = reemplazo_punto.split(" ")

contador = 0
buscar = input("¿Qué palabra desea buscar del texto?: ")
for i in range(len(separar)):
    if separar[i] == buscar:
        contador += 1
print(f"La palabra {buscar} aparece {contador} una vez/veces.")

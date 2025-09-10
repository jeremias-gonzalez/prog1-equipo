#1)
cadena="quíero comer manzañAs, solamente manzanas"
letra= "a"
def funcion1 (letra,cadena):
    return cadena.count(letra)
print(funcion1(letra,cadena))

#2)
def funcion2 (cadena):
    return cadena.replace("manzanas","peras")
print(funcion2(cadena))

#3)
def funcion3 (cadena):
    contador = 0
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    for letra in cadena:
        letra = letra.lower()
        letra = letra.strip()
        letra = letra.upper()
        if letra == "O" or letra == "A" or letra == "E" or letra == "I" or letra == "U":
            contador += 1
        elif letra == "o" or letra == "a" or letra == "e" or letra == "i" or letra == "u":
            contador1 += 1
        elif letra == "Á" or letra == "É" or letra == "Í" or letra == "Ó" or letra == "Ú":
            contador2 += 1
        elif letra == "á" or letra == "é" or letra == "í" or letra == "ó" or letra == "ú":
            contador3+= 1
        elif letra == "ñ":
            contador4 += 1
        elif letra == "Ñ":
            contador5 += 1
    return (contador, contador1, contador2, contador3, contador4, contador5)
print(funcion3(cadena))
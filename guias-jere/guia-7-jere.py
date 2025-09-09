#1)
cadena="quiero comer manzanas, solamente manzanas"
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
    for letra in cadena:
        letra = letra.lower()
        letra = letra.strip()
        letra = letra.upper()
        if letra == "O" or letra == "A" or letra == "E" or letra == "I" or letra == "U":
            contador += 1
    return contador
print(funcion3(cadena))
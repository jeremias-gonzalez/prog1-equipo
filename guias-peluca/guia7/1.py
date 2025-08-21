texto = "Quiero comer manzanas, solamente manzanas."

def contador_letras_repetidas(cadena, letra):
    contador = 0 
    for x in cadena:
        if x == letra:
            contador += 1

    return contador 

letraxd = input ("QUE LETRA QUIERE BUSCAR?: ")
resultado = contador_letras_repetidas (texto, letraxd)
print (f"La cantida de veces que se repite esa letra es {resultado}")
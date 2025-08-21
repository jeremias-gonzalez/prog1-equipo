texto = "Quiero comer manzanas, solamente manzanas."

def cambiador_palabras(texto, palabra, nueva_palabra):
    return texto.replace(palabra, nueva_palabra)


nuevo_texto = cambiador_palabras(texto, "manzanas", "peras")
print(nuevo_texto)


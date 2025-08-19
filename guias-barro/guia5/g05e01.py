# 1) Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python". 
# Cortar la cadena original, agregarle el literal "Programación en" y concatenar.

cadena = ("Curso de python")

separar = cadena.split()
separar.insert(2, "Programación")
separar.insert(3, "en")
cadena = " ".join(separar)
print(cadena)

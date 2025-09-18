#1) Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python". 
#Cortar la cadena original, agregarle el literal "Programación en" y concatenar. 
#Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido.

cadena = "Curso de Python"

separar = cadena.split()
separar.insert(2, "Programación en")
juntar = " ".join(separar).lower()
print(juntar)
#10) Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena.
#Ej.: 'Juan tiene 25 años' mostraría el número 50.

cadena = 'Juan tiene 25 años'
separar = cadena.split(" ")
numero = int(separar[2]) * 2
separar[2] = str(numero)
juntar =" ".join(separar)
print(juntar)
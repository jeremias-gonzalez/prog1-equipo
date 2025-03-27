nombre = input ("Ingresa tu nombre: ")
edad = int (input ("Ingresa tu edad: "))

pasaje = int (20000)
descuento = int (20000 * 0.40)
if edad >=5 and edad <= 10 :
    print (f"{nombre} de {edad} años tiene un costo de pasaje de ${pasaje - descuento} ")
elif edad >=65 :
     print (f"{nombre} de {edad} años tiene un costo de pasaje de ${pasaje - descuento} ")    

else:
    print (f"{nombre} de {edad} años tiene un costo de pasaje de ${pasaje} ")      
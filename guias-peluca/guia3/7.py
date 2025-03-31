
pregunta ="si"
contador = 0
while pregunta == "si":
      auto = str (input ("Ingrese el auto: "))
      precio = int (input ("Ingrese el precio: "))
      if precio >= 27460000 and precio <= 33850000:
          contador = contador + 1
    

      pregunta=input("Queres seguir? Si / No ")
      

      
    
print(f"La cantidad de autos en ese rango de precio es {contador}")
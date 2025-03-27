n1 = input ("Ingresa un numero: ")
n2 = input ("Ingresa otro numero: ")

n1 = int (n1)
n2 = int (n2)

if n1 > n2 :
    print (f"{n1} es mayor que {n2}")
elif n1 == n2:
    print (f"Son iguales")
else:
    print (f"{n1} es menor que {n2}")        

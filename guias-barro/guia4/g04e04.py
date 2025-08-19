#4) Dada una lista con números, 
# crear otra con los cuadrados de esos valores. 

n = []
n_elevados = []

while True:
    numero = int(input("Ingrese un número: "))
    pregunta = input('Desea ingresar otro número? (si/no): ')
    if pregunta == "no":
        break
    n.append(numero)
for i in n:
    n_elevados.append(i ** 2)
print(n_elevados)


    
    


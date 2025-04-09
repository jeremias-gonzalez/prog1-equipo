#1)
# listNum=[]
# contador =0
# for num in range (10):
#     num = int(input("Ingrese un numero:"))
#     if num > 23 :
#         contador  = contador +1
#         listNum.append(num)

# print(f"Los numeros son {listNum} y la cantidad es {contador}")

#2)
#Cargar letras en una lista hasta que el usuario ingrese un asterisco
#Luego hacer otra iteración para contar las vocales. Al final mostrar el total.
# letras =[]
# pregunta = "s"
# totalVocales = ["a","e","i","o","u"]
# contador=0
# otralista= []
# while pregunta == "s":
#  letra = input("carga una letra: ")
#  letras.append (letra)
#  pregunta = input("Si no quieres seguir ingresando letras presiona * sino s: ")
# for letrita in letras:
#       if letrita in totalVocales :
#           otralista.append(letrita)
#           contador = contador + 1
         
# print(f"el total de vocales ingresadas son {contador} y {otralista}")

#3)
names = []
sex = []
otherSex= []
question = "s"
contador=0

while question == "s":
    nm = input("ingresa un nombre:")
    sx = input("ingresa el sexo:")
    names.append(nm)
    sex.append(sx)
    question = input("quieres seguir ingresando:")
    for i in range(len(sex)):
     if sex[i] == "fem":
        otherSex.append(names[i])

    # contador = contador+1   
    
    
print(otherSex)
        
        
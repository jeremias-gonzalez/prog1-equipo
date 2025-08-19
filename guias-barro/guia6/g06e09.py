#9) Primer bucle: Almacenar nombres y sexos de personas hasta que el usuario diga que no hay más. 
cosas = [

]

while True:
    nombres_y_sexos = {}
    nombres_y_sexos["Nombre"] = input("Ingrese un nombre: ")
    nombres_y_sexos["Sexo"] = input("Ingrese su sexo: ")
    cosas.append(nombres_y_sexos)

    pregunta = input("Hay más usuarios para ingresar? (No/Si): ")
    if pregunta == "No":
        break
    if pregunta != "Si":
        print("!No es una respuesta adecuada, vuelva a intentarlo!")
        break

#Segundo bucle: Recorrer y guardar los nombres de las mujeres en una lista.

lista_mujeres = []

for i in cosas:
    if i["Sexo"] == "Femenino":
        lista_mujeres.append(i["Nombre"])
print(lista_mujeres)

#Tercer bucle: Mostrar los elementos de la lista resultante.
for nombre in lista_mujeres:
    print(nombre)
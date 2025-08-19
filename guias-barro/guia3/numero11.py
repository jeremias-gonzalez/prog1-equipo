#11) Pedir nombres y sexo de personas 
# y mostrar el total de mujeres y el nombre de cada una.
nombre = ""
variable_con_nombres = ""
total = 0
mujeres = 0

while True:
    nombre = input("Ingrese su nombre, por favor: ")
    sexo = input('ingrese el sexo de la persona: ')
    if sexo == "mujer" or sexo == 'Mujer':
        total += 1
        mujeres = total
        variable_con_nombres = variable_con_nombres + ", " + nombre
    pregunta = input('Desea ingresar otra persona? (si/no): ')
    if pregunta == 'no':
        break
print(f'La cantidad de mujeres son: {mujeres}')
print(f'El nombre de cada una es: {variable_con_nombres}')


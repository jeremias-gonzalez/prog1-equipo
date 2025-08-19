#9) Dada una serie de nombres y de salarios respectivos. 
# determinar el salario mínimo. 
# y mostrar el nombre de la persona que menos gana.
queso = True

while True:
    personas = str(input("Ingrese el nombre de la persona: "))
    salario = int(input("Ingrese el salario: $")) 
    if queso:
        pobre = salario
        persona_menor = personas
        queso = False
    elif salario < pobre:
        pobre = salario
        persona_menor = personas
    pregunta = str(input("Desea ingresar otro nombre? (si/no): "))
    if pregunta == "no":
        break    
print(f'La persona con menor salario es {persona_menor} con un salario de {pobre}')

#7) Eliminar todos los valores iguales de una lista. 
# Previamente, solicitar el valor que quiero eliminar y si no está, 
# mostrar un cartel diciendo que no lo ha encontrado.

valores_repetidos = ["a", "a", "b", "b", "c", "d"]


while True:
    contador = 0
    pregunta = input(f'¿Qué valor repetido desea eliminar de la lista?({valores_repetidos}): ')
    if pregunta in valores_repetidos:
        for i in valores_repetidos:
            if pregunta == i:
                contador += 1
                valores_repetidos.remove(pregunta)
            
        """
            elif i == 1:
            print('Es un solo caracter')
        """

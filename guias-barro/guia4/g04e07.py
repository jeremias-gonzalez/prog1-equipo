#7) Eliminar todos los valores iguales de una lista.
# Previamente, solicitar el valor que quiero eliminar y si no está, 
# mostrar un cartel diciendo que no lo ha encontrado.

lista_valoresIguales = ['A', 'A', 'o', 'o', 'p', 'r', 'w', 'z', 'u', 'u']
contador = 0
while True:    
    valor_a_eliminar = input('¿Qué valor de la lista que sea igual desea eliminar?: ')

    if valor_a_eliminar in lista_valoresIguales:
        for i in lista_valoresIguales:
            if i == valor_a_eliminar:
                contador += i
                print(contador)
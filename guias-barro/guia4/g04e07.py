#7) Eliminar todos los valores iguales de una lista.
# Previamente, solicitar el valor que quiero eliminar y si no está, 
# mostrar un cartel diciendo que no lo ha encontrado.

lista_valoresIguales = ['A', "A", 'A', 'o', 'o', 'p', 'r', 'w', 'z', 'u', 'u']

while True:
    contador = 0    
    valor_a_eliminar = input('¿Qué valor de la lista que sea igual desea eliminar?: ')

    if valor_a_eliminar in lista_valoresIguales:
        for i in lista_valoresIguales:
            if i == valor_a_eliminar:
                contador += 1
        
        if contador > 1:
            for i in range(contador - 1):
                lista_valoresIguales.remove(valor_a_eliminar)

            print(lista_valoresIguales)
        elif contador == 1:
            print('Ese valor está solo una vez')
            print(lista_valoresIguales)
        
    else:
        print("El valor no está en la lista")
        print(lista_valoresIguales)
        break
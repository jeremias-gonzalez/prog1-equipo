#7) Eliminar todos los valores iguales de una lista.
# Previamente, solicitar el valor que quiero eliminar y si no está, 
# mostrar un cartel diciendo que no lo ha encontrado.

lista_valoresIguales = ['A', 'A', 'o', 'o', 'p', 'r', 'w', 'z', 'u', 'u']

while True:
    contador = 0    
    valor_a_eliminar = input('¿Qué valor de la lista que sea igual desea eliminar?: ')
    break
for i in range(len(lista_valoresIguales)):
    if valor_a_eliminar in lista_valoresIguales:
        if lista_valoresIguales[i] > 1:
            contador += 1
        lista_valoresIguales.remove(contador)
print(lista_valoresIguales)        

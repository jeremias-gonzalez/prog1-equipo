#1
def concatenar(*args, conector=' '):
    
    return conector.join(args)
"""el metodo .join() actua como separador de los elementos pasados
argumentos. por ende para entenderlo de mejor manera le estamos diciendo
que se interponga en la cantidad de args que se quiera."""

# Ejemplos de uso de la función
print(concatenar('hola', 'pibe'))
print(concatenar('hola', 'pibe', conector='@'))
print(concatenar('techo', 'mesa', 'árbol', conector='###'))
print(concatenar('techo', 'mesa', 'árbol', conector='|||||||'))

#2
"""
def contarSubCadena(cadena_principal, subcadena, ignorarMayusculas=True):
    if ignorarMayusculas:
       
        return cadena_principal.lower().count(subcadena.lower())
    else:
       
        return cadena_principal.count(subcadena)

frase = 'Desde niña me encanta mirar la luna, por eso es que le puse de nombre Luna a mi hija'

print(contarSubCadena(frase, 'luna')) 

print(contarSubCadena(frase, 'luna', ignorarMayusculas=False)) 
"""
#3
def promedio (*args,sinNegativos=False):
    suma=0
    longitud = len(args)
    for i in args :
        suma += i
        if i > 0 and sinNegativos == True :
            print(suma)
            resultado = (suma/longitud)
        else: 
            resultado = int(suma/longitud)
    return resultado
print(promedio(121,65,-88,34,-9,27))
print(promedio(121,65,-88,34,-9,27, sinNegativos=True)) # 247/4=61.75
print(promedio(2,4)) # 3


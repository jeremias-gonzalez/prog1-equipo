"""
tupla_nombres = ("Juan", "Zoe", "Andrea", "Marcelo")
a, b, c, d = tupla_nombres
print(a, b, c, d)
print(type(tupla_nombres))

def bar():
    return 29

print(bar())
"""
"""
#funcion parametro
def raya():
    for x in range(20): 
        print("-", end="")

raya()


def raya(cantidad, caracter): # parámetros: cantidad, caracter
    for x in range(cantidad): 
        print(caracter, end="")
    print()

raya(20, "-") # argumentos: 20, "-" # reemplazan a los parámetros 
raya(10, "+") # argumentos: 10, "+" # 10 reemplaza a cantidad y + a caracter
raya(30, "$") # argumentos: 30, "$"

# Salida:
 Las 3 comillas son otra forma de comentario para multilíneas
--------------------
++++++++++
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
"""
#Tipo: funcion procedimiento
def saludo(nombre):
    print("Hola", nombre)

saludo("Ana")


def saludo(nombre):
    return "Hola " + nombre # el signo + entre dos strings las concatena

print(saludo("Ana"))

def doble(numero):
    print(numero*2)

doble(3)

def doble(numero):
    return numero*2

print(doble(3))
print(f'El doble del doble es {doble(4) * 2}')
doble_de_9 = doble(9)
print(doble_de_9)
"""
"""
def operar(operacion, n1, n2): # 3 parámetros: string, número, número
    if operacion == 'suma':
        resultado = n1 + n2 # resultado es una variable local
    elif operacion == 'resta':
        resultado = n1 - n2 
    else:
        resultado = f'Operación desconocida "{operacion}"'
    return resultado

 # error!!! esta variable solamente existe dentro de la función
print('Resultado de la suma de 4+5: ', end='')
print(operar("suma", 4, 5)) # mismo orden que los parámetros
a = 2
b = 3
print(f'{a=} y {b=}')
print('Resultado de la resta:', operar("resta", a, b))
salida = operar('mutiplicación', 10, 4) # asigno el retorno a una variable
print(salida)
print(f'a * 3 + 10 (a vale 2): {operar('suma', a*3, 10)}')
otra_salida = operar(7, 5, 'resta') # error!!! orden incorrecto
print(operar('suma', 1, 2, 3)) # error!!! cantidad incorrecta de argumentos
"""
"""
def foo1(a, b, *args, n1="ene uno", **kwargs):
    print('foo1')
    print(a, b, args, n1, kwargs)
foo1(1, 2, 3, 4, 5, xX="equisequis", n1="<nuevo ene uno>", nN="algo")
foo1("a", "b") # los únicos argumentos obligatorios son los que corresponde a parámetros posicionales
"""
# variante posicionales exclusivos (positional-only arguments)
def foo3(a, b, /, c): 
    print('foo3')
    # la / obliga a NO usar el nombre del parámetro 
    #de los que quedan a la izquierda
    print(a, b, c)
foo3(1, 2, c=3) # solamente funciona si NO se pone a= y b=
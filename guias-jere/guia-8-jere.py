#1
def concatenacion(palabra1,*args,**kwargs):
    print(f"{palabra1}{args}{kwargs}")

print(concatenacion('hola', 'pibe',''))
print(concatenacion('hola', 'pibe','@'))
print(concatenacion('techo', 'mesa', 'árbol', '###'))
print(concatenacion('techo', 'mesa', 'árbol', '|||||||'))
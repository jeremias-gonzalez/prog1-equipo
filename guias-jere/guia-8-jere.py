#1
def concatenacion(palabra1,*args,conector=" "):
    args1="".join(args)
   
    if conector!="":
        return f"{palabra1}{conector}{args1}"
    elif args1!="":
        return f"{palabra1} {args1}"

print(concatenacion('hola', 'pibe'))
print(concatenacion('hola', 'pibe', conector='@'))
print(concatenacion('techo', 'mesa', 'árbol', conector='###'))
print(concatenacion('techo', 'mesa', 'árbol', conector='|||||||'))

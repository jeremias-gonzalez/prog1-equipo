#Recibir por teclado una cadena de números, dejarlo en formato string e insertar un punto cada 3 dígitos como divisorio de miles. 
#Ej.  “1234567890” debería devolver “1.234.567.890”


texto = "La vida la vida es un carruzel"

letra = input('¿Qué letra le gustaría saber cuantas veces se repite?: ').lower()
contador = 0
for i in range(len(texto)):
    if letra == texto[i]:
        contador += 1
print(f"La letra {letra} se repite: {contador} veces")

#3) Recibir por teclado una cadena de números, dejarlo en formato string e insertar un punto cada 3 dígitos como divisorio de miles. 
# Ej: “1234567890” debería devolver “1.234.567.890”

numero = "1234567890"
nuevo = ""
contador = 0
invertir = numero[::-1]
for i in range(len(invertir)):
    nuevo += invertir[i]
    contador += 1

    if contador % 3 == 0:
        nuevo += "."

print(nuevo[::-1])

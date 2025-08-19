# 2) Recibir por teclado una cadena de números,
# dejarlo en formato string e insertar un punto cada 3 dígitos como divisorio de miles.
# Ej. “1234567890” debería devolver “1.234.567.890”


numero = input("Ingrese números: ")

dividir = ".".join(numero)
cadena = dividir.split(".")
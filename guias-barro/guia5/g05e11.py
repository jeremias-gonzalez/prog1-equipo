#11) Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez)
# y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).

nombre_completo = ""
ingresar = input("Ingrese solo su nombre completo (sin coma de por medio): ")
nombre_completo += ingresar
separar = nombre_completo.split(" ")
apellido = separar[-1]
nombres = separar[:-1]
juntar = "".join(nombres)

print(f"{apellido}, {juntar}")



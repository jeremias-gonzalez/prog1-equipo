#1)
nombreCompleto=["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana","Santamaria, Carlos","Skarsgard, Azul","Catalejos, Walter"]
departamento=["Logistica","Desarrollo","Desarrollo","Logistica","Administracion", "Logistica","Desarrollo"]
fechaDeNacimiento=["15/05/1943","07/04/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
resultado=""
resultado2=""
for i in nombreCompleto:
    resultado = i[8:8]
    resultado2 = i[0:8]

print(f"{resultado}. {resultado2}")
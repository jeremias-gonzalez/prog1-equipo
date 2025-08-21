personas = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-06-1994",
    "Adeline LaPadula,France,18-06-2002",
    "Willy Branscombe,Argentina,21-11-1997",
    "Diane Piffe,France,07-08-1993",
    "Britta Causbey,France,24-04-1991",
    "Elisabeth Cleeve,France,04-03-1991",
    "Rafael Ivanchenkov,France,28-04-2002",
    "Zerk Milsom,Norway,03-12-1994",
    "Adorne Ovington,United States,17-08-1991",
    "Kathryn Backshell,United States,04-10-1992",
    "Blake Colbeck,United States,18-01-1999",
    "Arron Bresnahan,United States,30-06-2001",
    "Deloria Dominguez,France,31-07-1990",
    "Grenville Aldersea,Argentina,11-01-2001",
    "Jemimah Haughian,Argentina,30-11-1998",
    "Con Gethen,United States,06-06-1992",
    "Roxie Igoe,France,31-03-2002",
    "Hollyanne Mottley,United States,05-01-1996",
    "Ambrosio Cadore,Norway,09-12-2002"
]

# 1) La cantidad de personas de Argentina.

buscador = 'Argentina'
def contador_personas(texto):
    argentinos = 0 
    for persona in texto:
        datos_persona = persona.split(",")
        if datos_persona[1] == buscador:
         argentinos +=1
    return argentinos
print(f'La cantidad de Argentinos es: {contador_personas(personas)}')

# 2) La cantidad de personas de un país ingresado por el usuario.

buscador = input ('Que pais quieres buscar')
def contador_personas(texto):
    argentinos = 0 
    for persona in texto:
        datos_persona = persona.split(",")
        if datos_persona[1] == buscador:
         argentinos +=1
    return argentinos
print(f'La cantidad de personas de ese pais es: {contador_personas(personas)}')

# 3) Los nombres de pila y las edades de las personas cuyo apellido comience con una letra solicitada al usuario.
letra_apellido = input("Ingrese la primera letra del apellido: ")


for persona in personas:
        datos_persona = persona.split(",")
        nombre_completo = datos_persona[0]
        apellido = nombre_completo.split(" ")[1]
        primera_letra_apellido = apellido[0]

if primera_letra_apellido == letra_apellido:
        fecha_nacimiento = datos_persona[2]
        dia, mes, ano = (fecha_nacimiento.split("-"))
        edad = 2025 - int(ano)
        nombre_de_pila = nombre_completo.split(' ') [0]

        print(f'Nombre: {nombre_de_pila}, Edad: {edad}')

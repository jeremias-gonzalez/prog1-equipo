#esta vez no le voy a comentarear el codigo profe , presione f5 y corralo nomás,

personas = [
    "Josefa Taponales,France(Europe),30-10-2007",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Priya Singh,India(Asia),17-01-2007",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]

"""
añoLimite = int(input("Ingrese el año para buscar nacimientos posteriores: "))
apellidos = []

for persona in personas:
    persona.split(",")
    nuevalista=persona.split(",")
    nombre = nuevalista[0]
    nombre = nombre.split(" ")
    apellido = nombre[1]
    pais = nuevalista[1]
    fecha = nuevalista[2]
    nuevaFecha = fecha.split("-")
    Fecha = nuevaFecha[2]
    FechaEntero = int(Fecha)
    if FechaEntero < añoLimite:
        apellidos.append(apellido)
        
print(f"Los apellidos de las personas nacidas antes del año {añoLimite} son: {apellidos}")
"""
"""
ingresePais = input("Ingrese pais: ")
paisAIngresar = []
contador = 0
for persona in personas:
    persona.split(",")
    nuevalista=persona.split(",")
    pais = nuevalista[1]
    if ingresePais in pais:
            contador = contador + 1
print(f"La cantidad de personas nacidas en {ingresePais} es: {contador}")
"""
ingreseContinente = input("Ingrese Continente: ")
personasNoEuropeas = []

for persona in personas:
    persona.split(",")
    nuevalista=persona.split(",")
    nombre = nuevalista[0]
    nombre = nombre.split(" ")
    nombre = nombre[0]
    pais = nuevalista[1]
    if ingreseContinente == "Europe" and ingreseContinente not in pais:
        nombre = nuevalista[0]
        nombre = nombre.split(" ")
        nombre = nombre[0]
        personasNoEuropeas.append(nombre)
        
print(f"Personas no Europeas:{personasNoEuropeas}")




 


#Quiero obtener: 
#1)Los apellidos de las personas nacidas antes de un año solicitado al usuario.
"""
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


año_nac = int(input("Ingrese un año: "))
print(f'Las personas nacidas antes del año {año_nac} son: ')
for i in personas:
    lista = i.split(",")
    nombre_apellido = lista[0]
    fecha_nacimiento = lista[2]
    apellido = nombre_apellido.split(" ")[1]
    año = int(fecha_nacimiento.split("-")[2])
    if año < año_nac:
        print(apellido)
"""

#2) La cantidad de personas nacidas en un país ingresado por el usuario.
"""
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


país = input("Ingrese un país: ")
contador = 0
print(f"La cantidad de personas del país {país} son: ")
for i in personas:
    lista = i.split(",")
    pais = lista[1]
    continente = pais.split("(")[0]

    if país == continente:
        contador += 1
print(contador)
"""

#3) Los nombres de pila de las personas que no son europeas.

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


for i in personas:
    pos_parentesis = i.find('(')
    inicio_continente = pos_parentesis + 1
    final_continente = i.find(')')
    continente = i[inicio_continente:final_continente]
    
    if continente != "Europe":
        pos_espacio = i.find(' ')
        print(i[:pos_espacio])
    
    
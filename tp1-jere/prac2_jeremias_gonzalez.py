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

for persona in personas:
    persona.split(",")
    nuevalista=persona.split(",")
    nombre = nuevalista[0]
    nombre = nombre.split(" ")
    nombre = nombre[1]
    pais = nuevalista[1]
    fecha = nuevalista[2]
    nuevaFecha = fecha.split("-")
    Fecha = nuevaFecha[2]
    FechaEntero = int(Fecha)
    FechaEntero =int(input("Ingrese año: "))
    apellidos_antes_del_anio = []
    if 2000 < FechaEntero:
        apellidos_antes_del_anio.append(nombre)
    
    if apellidos_antes_del_anio:
        print("Los apellidos de las personas nacidas antes de ese año son:", apellidos_antes_del_anio)
    else:
        print("No hay personas nacidas antes de ese año.")
    
  # else:
        #     print("No hay personas nacidas antes de ese año")
        # print("Apellido: ", nombre)
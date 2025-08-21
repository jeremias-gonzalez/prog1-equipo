from datetime import datetime
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

pais=[]
# ingresar = input("Ingrese un pais: ")
#mediante una funcion obtener la cantidad de personas de Argentina

# def cantidadPersonas (mensaje=""):
   
#     contador = 0
#     print("Opciones: ['Germany', 'United States', 'Norway', 'France']")
#     ingresar = input("Ingrese otro país además de Argentina: ")
    
#     for i in personas :
        
#         p = i.split(",")
#         pais.append(p[1])
#         pass

#     # for x in pais:
#     #       if x == "Argentina":
#     #        pass
#     #        contador += 1
#     if ingresar in pais:
#              for paisx in pais:
#                  if ingresar == paisx:
#                   contador += 1 
         
#              mensaje = print(f"La cantidad de personas en {ingresar} es {contador}")
#     else:
#         print("Opción inválida")
#     return mensaje
# print(cantidadPersonas(mensaje=""))
# return print("La cantidad de personas de Argentina es", contador)
                  
def inicialApellido(nombre="", inicial="", calculo=0):
    inicial = input("Ingrese una inicial de apellido: ").strip().upper()

    for i in personas:
        p = i.split(",")
        nombre_completo = p[0].split()
        fecha_nacimiento = p[2]
        
        if len(nombre_completo) < 2:
            continue

        apellido = nombre_completo[1]

        if apellido.upper().startswith(inicial):
        
            dia, mes, año = map(int, fecha_nacimiento.split("-"))
            fecha_nac = datetime(año, mes, dia)
            hoy = datetime(2025, 8, 21)
            edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

            print(f"{nombre_completo[0]} tiene {edad} años")


print(inicialApellido())




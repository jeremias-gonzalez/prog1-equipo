#1)
nombreCompleto=["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana","Santamaria, Carlos","Skarsgard, Azul","Catalejos, Walter"]
departamento=["Logistica","Desarrollo","Desarrollo","Logistica","Administracion", "Logistica","Desarrollo"]
fechaDeNacimiento=["15/05/1943","07/04/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]

# for i in nombreCompleto:
#     #recorremos desde la posicion 0 toda la lista
#        partes = i.split(", ")
#     #partes junto a un split en la posicion ,
#     #convierte en una sublista ["apellido","nombre"], quitando la coma y el espacio siguiente
#        posicion = partes[1]
#        #posicion toma la posicion 1 de la sublista hecha con split[,"Ana"]
#        inicial= posicion[0]
#        #inicial toma la posicion 0 de la posicion 1["A"]
#        segundaposicion= partes[0]
#        #posicion toma la posicion 0 de la sublista hecha con split["Torres",]
#        apellido= segundaposicion[:11]
#        #establecemos un limite de 11 posiciones ya que todos los apellidos tienen una longitud diferente
#        print(f"{inicial}. {apellido}")
#        #printeamos el resultado esperado.
#        #correcto.

# for x in nombreCompleto:
 #recorremos desde la posicion 0 toda la lista
#        separar= x.split(", ")
     #   nombre = separar[:6]
     #   nombreLargo = separar[1] 
    #hasta aqui repetimos todo el proceso de manera similar al bucle anterior
     #   for q in range (len(nombreLargo)):
    #recorremos toda la longitud de la sublista con q desde la posicion 0
     #     if q in range (len(nombreLargo)) and q > 5 : 
     #si q se encuentra en el rango de la longitud de la sublista y q es mayo a 5
     #es decir si la posicion contiene mas de 5 lugares.
     #      print("El nombre más largo es:",nombreLargo)
     #imprimi la posicion esperada
     #Benicio.

# suma_edades = 0 
# contador = 0 
# for d in range(len(departamento)):#recorre la longitud de la lista en desde la posicion 0 con d  
#     if departamento[d] == "Logistica":
#         #aca decimos que si lo recorrido coincide con Logistica ya que estamos trabajando sobre listas paralelas que ejecute lo siguiente:
#         fecha = fechaDeNacimiento[d]
#          #guardamos la posicion paralela de departamento en fecha de nacimiento con una variable 
#         separar = fecha.split("/")
#         #quitamos el slash con un split ya que lo que queremos es dejar la posicion año de manera individual como entero  
#         año = int(separar[2])
#         #tomamos y convertimos esa posicion en entero asignandola a otra variable
#         edad = 2025 - año
#         #de manera un tanto tradicional calculamos el año actual menos la posicion 
#         suma_edades = suma_edades + edad
#         #variable acumuladora y encargada de sumar cada posicion(edad) recorrida de la lista
#         contador = contador + 1
#         #contador es el responsable de contabilizar cuantas personas hay dentro del mismo departamento.        
#         print(f"la edad de {nombreCompleto[d]} es de {edad} y es del departamento de {departamento[d]}")
#         #hacemos un print para corrobar si arroja el resultado previo esperado
#         #arrojó el resultado esperado.


# promedio =int(suma_edades / contador)
# #como dice la variable asignada estamos buscando un promedio 
# #entre la cantidad de personas que conforman el departamento junto a sus edades
# print("El promedio de edad de las personas del Departamento de Logística es de:", promedio)
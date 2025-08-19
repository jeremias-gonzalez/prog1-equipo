#1) La diferencia en cantidad de bebés que existe entre los nombres de misma posición y mismo sexo. 
# Se solicita posición y sexo. (Ver salidas de ejemplo).


nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

m = []
f = []
split = nacidos2008.split(",")    
print(split)

for i in split:
    print(split[i+1])

#3) Crea un diccionario con los nombres de tus amigos como claves y sus alturas como valores. 
# Luego, itera sobre el diccionario e imprime cada nombre seguido de su altura y un cartel al lado que diga "(es alto)" cuando supere el metro ochenta. 
#Salida ejemplo:
#Pipo mide 1.65
#Pocho mide 1.90
#Laura mide 1.55 (es alto)

nombres_dic = {"Juan": 1.80, "Ignacio": 1.84, "Jere": 2.0, "Marcos": 1.82}

for k, v in nombres_dic.items():
    if v > 1.80:
        print(k, "mide", v, "es alto")
    elif v >= 1.80:
        print(k, "no es alto")
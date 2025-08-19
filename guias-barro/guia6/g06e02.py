#2) Dado el siguiente diccionario: inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "camisas": 8}, 
# elimina el artículo zapatos y duplica las cantidades de todos los otros artículos. Muestra el inventario actualizado.

inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "camisas": 8}

borrar = inventario.pop("zapatos")

for i in inventario:
    inventario[i] *= 2
print(inventario)

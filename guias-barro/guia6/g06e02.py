#2) Dado el siguiente diccionario: inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "camisas": 8},
# elimina el artículo zapatos y duplica las cantidades de todos los otros artículos. 
# Muestra el inventario actualizado.

inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "camisas": 8}

zapatos = inventario.pop("zapatos")
"""
inventario["camisetas"] = 20
inventario["pantalones"] = 5 * 2
inventario["camisas"] = 8 * 2
"""
for v in inventario:
    inventario[v] *= 2
print(inventario)

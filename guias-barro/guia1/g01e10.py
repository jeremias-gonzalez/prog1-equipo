# Si una persona consume 2.5 litros de nafta por día
# Y decide dejar de consumir Infinia ($1459 x litro) para pasarse a Super ($1216 x litro),
# Cuánto ahorrará en un año? (suponiendo que no cambien los precios).
# Salida: Para los datos referidos de consumo (2.5 litros de nafta por día) y los precios de los tipos de nafta, 
# Tu ahorro anual, suponiendo precios estables, será de $221737.50

infinia = float(1459 * 2.5)
super = float(1216 * 2.5)

print(f'Lo que gastaba en infinia por día es de ${infinia}, y lo que gasta en super por día es de ${super}')
print(f'Por lo que, se ahorra por año es de ${infinia * 365 - super * 365}')

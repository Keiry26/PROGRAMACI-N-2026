"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.

total = sum(consumos_litros)
promedio = total / len(consumos_litros)

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]
ahorro = primer_dia - ultimo_dia
porcentaje = (ahorro / primer_dia) * 100

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.

if porcentaje >= 15:
    clasificacion = "Reducción alta"
elif porcentaje > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"

# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.

print("RESULTADOS DEL CONSUMO DE AGUA")
print("--------------------------------")
print(f"Consumo total: {total} litros")
print(f"Promedio diario: {promedio} litros")
print(f"Litros ahorrados: {ahorro} litros")
print(f"Porcentaje de reducción: {porcentaje:.0f}%")
print(f"Clasificación: {clasificacion}")
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
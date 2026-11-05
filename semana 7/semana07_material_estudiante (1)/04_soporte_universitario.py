"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.

"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Preparar las variables

total_minutos = 0
categorias = {
    "Acceso": 0,
    "Equipo": 0,
    "Red": 0
}

pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
caso_mas_largo = ("", 0)

# Recorrer las incidencias

for caso in incidencias:
    total_minutos = total_minutos + caso["minutos_atencion"]

    # Contar las categorías

    categorias[caso["categoria"]] = categorias[caso["categoria"]] + 1

    # Revisar los casos pendientes

    if caso["resuelto"] == False:
        pendientes = pendientes + 1
        provincias_pendientes.add(caso["provincia"])
        # Identificar los casos urgentes

        if caso["minutos_atencion"] >= 60:
            casos_urgentes.append((caso["id"], caso["minutos_atencion"]))
    # Buscar el caso con más minutos
    if caso["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (caso["id"], caso["minutos_atencion"])

# Calcular el promedio

promedio = total_minutos / len(incidencias)

# Comprobar si San Jose tiene casos pendientes

hay_san_jose = "San Jose" in provincias_pendientes

# Mostrar los resultados

print("ANÁLISIS DE INCIDENCIAS")
print("-----------------------")
print(f"Total de casos: {len(incidencias)}")
print(f"Total de minutos: {total_minutos}")
print(f"Promedio de minutos: {promedio}")
print("\nCasos por categoría:")
print(f"Acceso: {categorias['Acceso']}")
print(f"Equipo: {categorias['Equipo']}")
print(f"Red: {categorias['Red']}")
print(f"\nCasos pendientes: {pendientes}")
print(f"Provincias con pendientes: {provincias_pendientes}")
print(f"Casos urgentes: {casos_urgentes}")
print(f"\nCaso con más minutos: {caso_mas_largo}")

if hay_san_jose:
    print("Hay pendientes en San Jose")
else:
    print("No hay pendientes en San Jose")

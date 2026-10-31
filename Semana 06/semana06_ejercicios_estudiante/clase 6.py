capacidad = 700
aceptados = []
rechazados = []
ocupacion = 0

entrada = input("Grupo (o fin para terminar): ").strip().lower()

while entrada != "fin":

   # if entrada.lower() == "fin":
        #break

    try:
        grupo = int(entrada)

        if grupo <= 0:
            print("Grupo inválido. Debe ser mayor que cero.")
            rechazados.append(grupo)

        elif grupo > capacidad:
            print("Grupo rechazado. Supera la capacidad del anfiteatro.")
            rechazados.append(grupo)

        elif ocupacion + grupo <= capacidad:
            aceptados.append(grupo)
            ocupacion += grupo
            print("Grupo aceptado.")

        else:
            print("Grupo rechazado. No hay suficiente espacio.")
            rechazados.append(grupo)

    except ValueError:
        print("Entrada inválida. Debe ingresar un número o 'fin'.")

    entrada = input("Ingrese la cantidad de personas del grupo (o escriba 'fin'): ")
# Análisis final
total_admitido = 0

if aceptados:
    menor = aceptados[0]
    mayor = aceptados[0]

    for grupo in aceptados:
        total_admitido += grupo

        if grupo < menor:
            menor = grupo

        if grupo > mayor:
            mayor = grupo
else:
    menor = 0
    mayor = 0

espacios_disponibles = capacidad - total_admitido
porcentaje = (total_admitido / capacidad) * 100

if porcentaje == 100:
    estado = "Capacidad completa"
elif porcentaje >= 75:
    estado = "Alta ocupación"
elif porcentaje >= 50:
    estado = "Ocupación media"
else:
    estado = "Baja ocupación"

print("\n----- REPORTE FINAL -----")
print("Grupos aceptados:", aceptados)
print("Grupos rechazados:", rechazados)
print("Total admitido:", total_admitido)
print("Espacios disponibles:", espacios_disponibles)
print(f"Porcentaje de ocupación: {porcentaje:.2f}%")
print("Grupo aceptado menor:", menor)
print("Grupo aceptado mayor:", mayor)
print("Estado final:", estado)

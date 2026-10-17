producto = ["Cafe", 5000, 20]
porcentaje_aumento=20
descuento= producto[1] * 15/100
precio_promocional= producto[1] - descuento
ingreso_actual = producto[1] * producto[2]
aumento = producto[2] * porcentaje_aumento / 100
suma_unidades = producto[2] + aumento
ingreso_proyectado = precio_promocional * suma_unidades
diferencia = ingreso_proyectado - ingreso_actual

print("\nANÁLISIS DE PROMOCIÓN\n")

print(f"Producto: {producto[0]}")
print(f"Precio actual: ₡{producto[1]}")
print(f"Unidades actuales: {producto[2]}")
print(f"Ingreso actual: ₡{ingreso_actual:.0f}")
print(f"Descuento: ₡{descuento:.0f}")
print(f"Precio promocional: ₡{precio_promocional:.0f}")
print(f"Aumento esperado en ventas: {porcentaje_aumento}%")
print(f"Unidades proyectadas: {suma_unidades:.0f}")
print(f"Ingreso con promoción: ₡{ingreso_proyectado:.0f}")
print(f"Diferencia: ₡{diferencia:.0f}")

if diferencia > 0:
    print("\nRECOMENDACIÓN: lanzar.")
else:
    print("\nRECOMENDACIÓN: no lanzar.")
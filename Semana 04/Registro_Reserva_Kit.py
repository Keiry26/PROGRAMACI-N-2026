#Solucion mision kit seguro

#ENTRADAS!!!

nombre= input("nombre: ").upper().strip()
kit= input("tipo de kit: ").lower().strip()
autorizacion= input("tiene autorizacion (si/no): ").lower().strip() == "si"
try: # intente hacer algo "plan a"
    cantidad = int(input ("cantidad de kits?: "))
    if cantidad <1:
        print("error, la cantidad minima es 1 ")
except ValueError: # si da error imprima lo siguiente "plan b"
    print("cantidad de kits invalida, digite del 1 al 100")
    cantidad: -1
try:
    dias= int(input("dias de prestamo:" ))
except ValueError: # si da error imprima lo siguiente "plan b"
    print("cantidad de dias invalidos, digite del 1 al 10")
    cantidad: -1
     
# PROCESO!!!!

if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado= "rechazado, revise los datos ingresados"
elif autorizacion and cantidad <= 3 and not dias <7:
    resultado= f'solicitud aprobada para {nombre} : {cantidad} kit(s) de {kit}'
else:
    resultado= "solicitud enviada a revision"
#SALIDA!!!

print('-' * 50,'\n')
print(resultado)




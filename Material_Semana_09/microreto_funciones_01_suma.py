"""Microreto independiente: sumar tiempos con una función y un acumulador."""


ESPERAS = [12, 20, 18]


def sumar_esperas(minutos):
    """Devuelve la suma de los minutos recibidos en horas."""
    total = 0 
    
    for minuto in minutos:
        # TODO: acumule cada minuto en total.
        total += minuto

    return total

#TODO: llame a la función sumar_esperas y guarde el resultado en una variable. Luego, imprima el resultado en horas.
resultado = sumar_esperas(ESPERAS)
horas = resultado / 60 
 
# Luego, imprima el resultado en horas.
print(f"El total de minutos de espera es: {resultado} minutos")
print(f"El total de horas es: {round(horas, 2)} horas")
 
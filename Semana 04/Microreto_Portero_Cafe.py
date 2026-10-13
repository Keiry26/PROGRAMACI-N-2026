"""Microreto: el portero del café."""
#lower()=convertir en minuscula
#upper()= convertir en mayuscula
#strip()= quitar los espacios 
nombre= input("como te llamas?: ").upper().strip()  
energia= int(input("cuanta energia tienes de 0 a 100?: "))
trae_cafe= input("traes cafe (si/no)?: ").lower().strip() == "si"

"""print(trae_cafe)
print(type(trae_cafe))
if trae_cafe:
    print("si,viene con cafe")"""
mensaje = ""
#si menos 50% y no tengo cafe: = descansar
if energia<50 and not(trae_cafe): #trae_cafe==false
   mensaje = "vaya a descansar"
# si 50% o mas o traigo cafe: = puede ingresar
elif energia>=50 or trae_cafe:
    mensaje = "puede ingresar"
# cualquier otro ecenario:= portero confundido: revisar respuestas
else: 
    mensaje= "revise respuestas"
print(f"{nombre}: {mensaje}")
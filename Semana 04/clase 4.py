nombre= input("como te llamas?: ").upper().strip()  
energia= int(input("cuanta energia tienes de 0 a 100?: "))
trae_cafe= input("traes cafe (si/no)?: ").lower().strip()
mensaje= ""
if energia<50 and not(trae_cafe): #trae_cafe==false
   mensaje = "vaya a descansar"
elif energia>=50 or trae_cafe:
    mensaje = "puede ingresar"
else:
    mensaje= "revise respuestas" 

print(f"{nombre} -> {mensaje}")
import time
def caminar():
    print("Caminando...")
    time.sleep(3)

def saltar():
    print("Saltando...")
    time.sleep(3)

def atacar():
    print("Atacar...")
    time.sleep(3)

#Utilizando un diccionario, ejecutar la acción que indique el usuario
motor = {"CAMINAR":caminar, "SALTAR":saltar,"ATACAR":atacar}
accion=None
while motor.get(accion)==None:
    accion = input("¿Qué quieres hacer (CAMINAR/SALTAR/ATACAR)?")
    if (motor.get(accion)!=None): 
        motor[accion]()      
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

accion = input("¿Qué quieres hacer (caminar/saltar/atacar)?")
#eval(accion+"()")
exec(accion+"()")
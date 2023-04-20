import time

def ejecutador(funcion):
    funcion()

def funcion1():
    print("Ejecutando tarea 1...")
    time.sleep(3)

def funcion2():
    print("Ejecutando tarea 2...")
    time.sleep(3)

def funcion3():
    print("Ejecutando tarea 3...")
    time.sleep(3)

f1 = funcion1
f1()

ejecutador(funcion2)

tareas = (funcion2, funcion1, funcion3, funcion2, funcion3, funcion1)
for t in tareas:
    t()
    #ejecutador(t) #Alternativa a t()


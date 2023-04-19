#Función básica
def saludar():
    print("Ola")

#Función con parámetro
def saludar_con_nombre(nombre : str) -> None:
    print(f"Hola, {nombre}")

#Función con parámetro y retorno
def get_saludo(nombre):
    return f"Hola, {nombre}"

#Función que recibe dos números y retorna el resultado de la suma
def sumar(n1 : float, n2 : float) -> float:
    return n1 + n2

#Función que resta dos números siendo el segundo opcional con valor 0
def restar(n1, n2=0):
    return n1-n2

print(restar(5))
print(restar(5,2))

#Función con varios parámetros opcionales DEBEN IR AL FINAL
def calcular(c1,c2=3,c3=8,c4=5):
    return c1+c2+c3+c4

print(calcular(5))#21
print(calcular(5,2))#20
print(calcular(5,c3=9))#Indicamos que el valor de un parámetro concreto

#Función con varios parámetros a los que llamamos desordenadamente
def modificar(p1, p2, p3):
    print(f"Modificando {p1},{p2},{p3}")

modificar(p2="loqueseaquesea",p1="loquesea",p3="otroloquesea")

#Función que recibe un número indeterminado de parámetros (de tipo str)
def funcion_versatil(*parametros):#Parámetro es una tupla
    for parametro in parametros:
        print(parametro)

funcion_versatil(1)
funcion_versatil(2,4)
funcion_versatil(4,"Hola",True)

#Función que recibe un número indeterminado de parámetros y uno opcional
def funcion_versatil_opcional(*args, opcional=0):
    for parametro in args:
        print(parametro)
    print(opcional)

funcion_versatil_opcional("Uno")
funcion_versatil_opcional("Uno",2)
funcion_versatil_opcional("Uno",2,True)
funcion_versatil_opcional("Uno",2,True,opcional=18)

#Ejemplo de uso de función zip 

ciudades = ["Santiago","A Coruña", "Lugo", "Vigo", "Pontevedra"]
poblacion = [100_000, 250_000, 97_000, 295_000, 83_000]
galicia = zip(ciudades, poblacion, strict=True)#strict provoca un error si las listas tienen tamaños diferentes
lista_galicia = list(galicia)

#Función que recibe una relación indeterminada de parámetros con su valor

def funcion_ultraversatil(**kvargs):
    for clave,valor in kvargs.items():
        print(clave,valor)

funcion_ultraversatil(nombre="Santiago",poblacion=100_000)
    













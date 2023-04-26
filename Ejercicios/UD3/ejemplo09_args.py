def calcular(sumando1, sumando2):
    if sumando1==sumando2:
        raise ValueError("Hay un error")
    
try:
    calcular(5,5)
except ValueError as ve:
    print(ve)#Hay un error
    print(ve.args)#Muestra una tupla con los parámetros del constructor
    ve.args=("Acabo de cambiar el mensaje de error",)
    print(ve)#"Acabo de cambiar el mensaje de error"
    
LIMITE = 10

#MÉTODO 'return'
def proveedor_datos():
    lista_datos = list(range(0,LIMITE))
    return lista_datos

#datos = proveedor_datos()#En este punto, datos es una lista de 1000 enteros
for dato in proveedor_datos():
    print(dato,end=":")

print()

#MÉTODO 'generador'
def generador_datos():
    lista_datos = list(range(0,LIMITE))
    for dato in lista_datos:
        yield dato

for dato in generador_datos():
    print(dato,end=";")
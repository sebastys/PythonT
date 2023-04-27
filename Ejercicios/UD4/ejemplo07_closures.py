def funcion_externa(nombre):
    def funcion_interna(numero):
        print(f"Soy {nombre} y tengo el numero {numero}")
    return funcion_interna

nombre="Carlos"
x = funcion_externa(nombre)
nombre="David"
y = funcion_externa(nombre)
x(4)
y(8)


def transformar(variable : object, valor : object) -> None:
    variable.nombre = valor

class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

x = Animal("Buey")
transformar(x, "Vaca")#El paso de un objeto como parámetro siempre es por REFERENCIA
print(x.nombre)


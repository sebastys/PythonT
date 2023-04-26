class ProductoMultimedia:
    pass

class Pelicula(ProductoMultimedia):
    activa = True
    def __init__(self, titulo, director) -> None:
        self.titulo = titulo
        self.director = director
        self.__presupuesto = 1_000_000

p = Pelicula("El Resplandor", "Stanley Kubrick")

#Función issubclass
print(issubclass(Pelicula, ProductoMultimedia))#True
print(issubclass(ProductoMultimedia, Pelicula))#False
print(issubclass(ProductoMultimedia,object))#True
print(issubclass(Pelicula,object))#True
#Función isinstance
print(isinstance(p,Pelicula))#True
print(isinstance(p,ProductoMultimedia))#True

print(Pelicula.__dict__)
print("--------------------")
print(p.__dict__)
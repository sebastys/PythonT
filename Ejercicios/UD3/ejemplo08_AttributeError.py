class Pelicula:
    activa = True
    def __init__(self, titulo, director) -> None:
        self.titulo = titulo
        self.director = director
        self.__presupuesto = 1_000_000
    def proyectar(self):
        pass

p = Pelicula("El Resplandor", "Stanley Kubrick")

print(hasattr(p, "titulo"))#True
print(hasattr(p, "premios"))#False
print(hasattr(p, "__presupuesto"))#False, está renombrado
print(hasattr(p, "_Pelicula__presupuesto"))#True, es el renombrado de __presupuesto
print(hasattr(p, "proyectar"))#True, pese a que es un método
print(hasattr(p, "activa"))#True, pese a que es un atributo de clase
print(hasattr(Pelicula, "titulo"))#False, ya que hasta que no se ejecuta el constructor no existe
print(hasattr(Pelicula, "activa"))#True
print(hasattr(Pelicula, "proyectar"))#True, pese a que es un método

#Alternativa 1 de control de los errores de acceso a atributos inexistentes
try:
    print(p.ingresos)
except AttributeError as ae:
    print(ae)

#Alternativa 2 de control de los errores de acceso a atributos inexistentes
if hasattr(p,"ingresos"):
    print(p.ingresos)
else:
    print("No existe el atributo ingresos")
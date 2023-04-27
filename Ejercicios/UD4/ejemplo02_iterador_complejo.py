class Factura:
    def __init__(self, nombre, estado) -> None:
        self.nombre = nombre
        self.estado = estado

class Administracion:
    def __init__(self) -> None:
        self.__facturas = [Factura("Uno","PENDIENTE"), Factura("Dos","PAGADO"), Factura("Tres","PENDIENTE")]

    def __iter__(self):
        self.indice = -1
        self.__facturas_pendientes = [factura for factura in self.__facturas if factura.estado=="PENDIENTE"]
        return self
    
    def __next__(self):
        self.indice += 1
        if (self.indice == len(self.__facturas_pendientes)):
            raise StopIteration
        return self.__facturas_pendientes[self.indice]

admin = Administracion()
for factura in admin:
    print(factura.nombre)
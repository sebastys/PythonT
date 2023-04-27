class Administracion:
    def __init__(self) -> None:
        self.__facturas = ["Factura1","Factura2","Factura3","Factura4"]

    def __iter__(self):
        self.indice = -1
        return self
    
    def __next__(self):
        self.indice += 1
        if (self.indice == len(self.__facturas)):
            raise StopIteration
        return self.__facturas[self.indice]

admin = Administracion()
for factura in admin:
    print(factura)

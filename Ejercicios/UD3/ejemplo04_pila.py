class Pila:
    def __init__(self) -> None:
        self.__datos = []

    def mostrar_datos(self):
        print(self.__datos)

    def push(self, elemento):
        self.__datos.append(elemento)#Implementas una pila - LIFO (Last In First Out)
        #self.__datos.insert(0,elemento)#Implementas una cola - FIFO (First In First Out)
        self.mostrar_datos()

    def pop(self):
        if len(self.__datos)==0:
            raise Exception("La pila está vacía")
        retorno = self.__datos.pop()
        self.mostrar_datos()
        return retorno

p1 = Pila()
p1.push(3)
p1.push("Hola")
p1.push(True)
try:
    print(p1.pop())
    print(p1.pop())
    print(p1.pop())
    print(p1.pop())
except Exception as e:
    print(e)
        
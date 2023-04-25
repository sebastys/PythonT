class CuentaBancaria:
    COMISION = 1 #Atributo de clase - "constante"

    def __init__(self, nombre, iban, saldo) -> None:
        self.nombre = nombre #Atributos de instancia o atributos de objeto
        self.iban = iban
        self.__saldo = saldo
        self.gastos_acumulados = 0

    def retirar_fondos(self, cantidad):
        if cantidad+CuentaBancaria.COMISION>self.__saldo:
            raise Exception("No hay fondos suficientes")
        self.__saldo-=cantidad
        self.__saldo-=CuentaBancaria.COMISION
        self.gastos_acumulados+=CuentaBancaria.COMISION

    def ingresar_fondos(self, cantidad):
        self.__saldo+=cantidad
        self.__saldo-=CuentaBancaria.COMISION
        self.gastos_acumulados+=CuentaBancaria.COMISION

    #Sobreescritura (overwrite) del método
    def __str__(self) -> str:
        return f"El saldo de la cuenta {self.iban} de {self.nombre} es {self.__saldo}"
    
    #Sobreescritura del método de comparación __eq__
    def __eq__(self, __value: object) -> bool:
        return self.__saldo==__value.__saldo

c1 = CuentaBancaria("Rebeca","1234567890",10_000)
c2 = CuentaBancaria("Constante","0987654321",10_000)
c1.en_rojo = True #Agregando un nuevo atributo en tiempo de ejecución
del c2.gastos_acumulados #Eliminar atributo en tiempo de ejecución
print(dir(c1))
print(dir(c2))

try:
    c1.retirar_fondos(8_000)
    c1.retirar_fondos(3_000)
except Exception as e:
    print(e)

print(c1)

c1 = CuentaBancaria("Rebeca","1234567890",10_000)
c2 = CuentaBancaria("Constante","0987654321",10_000)
print(c1==c2)
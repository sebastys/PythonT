class Barco:
    #Constructor
    def __init__(self, _matricula, _eslora, _manga, _calado) -> None:
        print("Ejecutando constructor")
        self.matricula = _matricula #Atributo self.matricula
        self.eslora = _eslora #Atributo self.eslora
        self.manga = _manga
        self.calado = _calado
        self.velocidad = 0 #Atributo self.velociad. No viene como parámetro del constructor.

    #Método
    def acelerar(self, incremento):
        print("Estoy acelerando...")
        self.velocidad+=incremento

    #Método
    def virar(self, grados):
        print("Estoy virando...")

b = Barco("M7773",8,2.3,2.4)#Instanciación -> Genera un objeto asignado a b
b.acelerar(0.1)#Invocación a un método

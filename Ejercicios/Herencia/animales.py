class Animal(object):#(object) no es necesario ponerlo
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"Soy un Animal({self.nombre}) y estoy comiendo...")

    def reproducir(self):
        print(f"Soy un Animal({self.nombre}) y me estoy reproduciendo...")

    def nacer(self):
        print(f"Soy un Animal({self.nombre}) y estoy naciendo...")

class Mamifero(Animal):

    def mamar(self):
        print(f"Soy un Mamifero({self.nombre}) y estoy mamando...")

    #Sobreescritura del método
    def reproducir(self):
        print(f"Soy un Mamifero({self.nombre}) y me estoy reproduciendo...")

    #Sobreescritura de método
    def nacer(self):
        #super().nacer() #Alternativa 1
        Animal.nacer(self) #Alternativa 2
        print(f"Soy un Mamifero({self.nombre}) y estoy naciendo...")

if __name__=='__main__':
    lagarto = Animal("Juancho")
    lagarto.comer()#Soy un Animal(Juancho) y estoy comiendo...
    lagarto.reproducir()#Soy un Animal(Juancho) y me estoy reproduciendo...
    #gato.mamar()
    perro = Mamifero("Alcanfor")
    #Lo que viene a continuación es consecuencia del polimorfismo
    perro.comer()#Soy un Animal(Alcanfor) y estoy comiendo...
    perro.mamar()#Soy un Mamifero(Alcanfor) y estoy mamando...
    perro.reproducir()#Soy un Mamifero(Alcanfor) y me estoy reproduciendo...
    perro.nacer()
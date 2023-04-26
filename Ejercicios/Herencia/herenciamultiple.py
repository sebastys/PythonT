from animales import Animal, Mamifero
from servivo import SerVivo

#Herencia múltiple
class Engendro(Mamifero, SerVivo):
    pass

if __name__=='__main__':
    shrek = Engendro("Shrek")
    shrek.reproducir()
    print(Engendro.__bases__)
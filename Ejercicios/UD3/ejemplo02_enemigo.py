'''
Clase Enemigo
- Atributos
- Métodos
Crear dos enemigos
Llamar a un método distinto en cada enemigo que 
muestre el valor de un atributo por pantalla
'''
class Enemigo(object):
    def __init__(self, _nombre, _vida, _velocidad) -> None:
        self.nombre = _nombre
        self.vida = _vida
        self.velocidad = _velocidad
        self.posicion = [0,0]
        self.__vivo = True #Atributo privado u 'oculto'
    
    #Método de acceso que encapsula la lectura del valor del atributo __vivo
    def get_vivo(self):
        return self.__vivo

    def __morir(self):#Definición de un método privado u 'oculto'
        print("Muriendo...")
        self.__vivo = False

    def recibir_impacto(self, danyo):
        print("Recibiendo daño...")
        self.vida-=danyo
        if self.vida<=0:
            self.__morir()

enemigo1 = Enemigo("Enemigo 1",10,1)
enemigo2 = Enemigo("Enemigo 2",10,2)
enemigo1.recibir_impacto(5)
enemigo1.recibir_impacto(3)
enemigo1.recibir_impacto(3)
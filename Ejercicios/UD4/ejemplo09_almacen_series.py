class Serie:
    x = 5
    def __init__(self, nombre, sinopsis, numero_temporadas) -> None:
        self.nombre = nombre
        self.sinopsis = sinopsis
        self.numero_temporadas = numero_temporadas

    def guardar(self):
        fichero = open(self.nombre + ".serie",mode="wt", encoding="utf-8")
        fichero.write(self.nombre + "\n")
        fichero.write(self.sinopsis + "\n")
        fichero.write(str(self.numero_temporadas) + "\n")
        fichero.close()

    def guardar_with(self):
        with open(self.nombre + ".serie",mode="wt", encoding="utf-8") as fichero:
            fichero.write(self.nombre + "\n")
            fichero.write(self.sinopsis + "\n")
            fichero.write(str(self.numero_temporadas) + "\n")

    def auto_guardar(self):
        fichero = open(self.nombre + ".serie",mode="wt", encoding="utf-8")
        for v in self.__dict__.values():
            fichero.write(str(v) + "\n")
        fichero.close()

if __name__=="__main__":
    lou = Serie("The Last of Us", "Un hombre y una niña luchan contra los zombies", 1)
    #lou.guardar()
    twd = Serie("The Walking Dead", "Unos zombies malos atacan", 8)
    #twd.guardar_with()
    fdg = Serie("Farmacia de guardia", "Una farmacia de barrio muy divertida", 3)
    fdg.auto_guardar()
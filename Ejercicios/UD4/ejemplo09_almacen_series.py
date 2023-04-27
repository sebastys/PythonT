class Serie:
    def __init__(self, nombre, sinopsis, numero_temporadas) -> None:
        self.nombre = nombre
        self.sinopsis = sinopsis
        self.numero_temporadas = numero_temporadas

    def guardar(self):
        #Guardar los datos de la serie en un fichero con el nombre de la
        #serie y la extensión .serie
        pass


lou = Serie("The Last of Us", "Un hombre y una niña luchan contra los zombies", 1)
lou.guardar()
twd = Serie("The Walking Dead", "Unos zombies malos atacan", 8)
twd.guardar()
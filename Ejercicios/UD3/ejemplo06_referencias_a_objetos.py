from __future__ import annotations #Evita que las referencias a clases declaradas más adelante den error. PROBAR A ELIMINAR ESTA LÍNEA

class CV:
    def __init__(self, dp : DatosPersonales, da : DatosAcademicos, ep : ExperienciaProfesional):
        self.dp = dp
        self.da = da
        self.ep = ep

    def mostrar_info(self):
        print(self.dp.nombre)

class DatosPersonales:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class DatosAcademicos:
    pass

class ExperienciaProfesional:
    pass

dp = DatosPersonales("Fernando")
da = DatosAcademicos()
ep = ExperienciaProfesional()

cv = CV(dp, da, ep)

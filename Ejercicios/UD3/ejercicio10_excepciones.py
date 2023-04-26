class LongitudMinimaException(Exception):
    pass

LONGITUD_MINIMA = 3
def validacion(nombre):
    if len(nombre)<LONGITUD_MINIMA:
        raise LongitudMinimaException("Longitud insuficiente")
    return True

try:
    validado = validacion("Pi")
except LongitudMinimaException as lme:
    print(lme)


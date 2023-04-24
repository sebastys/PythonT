cadena = "Me gusta programar en Python"
cadena_busqueda = input("Introduce los caracteres a buscar:")
'''
Utilizandos index (puede provocar ValueError -gestionarlo-) y slicing.
Obtener dos cadenas:
- Una con lo que hay antes de lo que estamos buscando
- Otra con lo que hay a partir de los que estamos buscando (incluido)
Ejemplo:
Buscando 'prog' muestra 'Me gusta ' y 'programar en Python'
'''
try:
    posicion = cadena.index(cadena_busqueda)#Obtenemos la posición de la cadena buscada
except ValueError:
    print("No he encontrado la cadena")
else:
    primera_parte = cadena[:posicion]
    segunda_parte = cadena[posicion:]
    print(primera_parte)
    print(segunda_parte)
finally:
    print("Fin del proceso")

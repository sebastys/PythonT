#Pedir una palabra
#Independientemente de si está escrita en mayúsculas o minúsculas
#Contar el número de veces que aparece en el texto
#Salida: La palabra XXXX ha aparecido XX veces en el texto.

#Opción 'guay' comando with
with open("elquijote.txt", mode="r", encoding="utf-8") as fichero:
    contenido = fichero.read()
palabra = input("Introduce una palabra:")
numero_veces = contenido.upper().count(palabra.upper())
print(f'La palabra {palabra} ha aparecido {numero_veces} veces en el texto.')

#Opción 'tradicional' open-close
'''
fichero = open("elquijote.txt", mode="r", encoding="utf-8")
contenido = fichero.read()
fichero.close()
print(contenido)
'''
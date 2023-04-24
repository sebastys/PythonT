with open("elquijote.txt", mode="r", encoding="utf-8") as fichero:
    contenido = fichero.read()
palabra = input("Introduce una palabra:")
try:
    posicion=0
    while True:
        posicion = contenido.index(palabra,posicion+1)
        texto = contenido[posicion-25:posicion+25].replace("\n"," ")
        print(texto)
except:
    print("Fin")
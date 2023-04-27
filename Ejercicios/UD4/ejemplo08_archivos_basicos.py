#Abrir en modo 'r' (read-lectura) si no existe -> FileNotFoundError
#Abrir en modo 'a' (append-añadir) si no existe -> Crea
#Abrir en modo 'w' (write-escribir) si no existe -> Crea y sobreescribe el contenido
#Abrir en modo 't' (texto) -> Valor por defecto
#Abrir en modo 'b' (binario)
fichero = open("datos.txt", mode="wt",encoding="utf-8")
fichero.write("Manzana\n")
fichero.write("Pera\n")
fichero.write("Piña")
fichero.close()

#Por defecto se abre de lectura y tipo texto
fichero = open("datos.txt", encoding="utf-8")
datos = fichero.read()#Lee todo
#print(datos)
fichero.close()

fichero = open("datos.txt", encoding="utf-8")
datos = fichero.read(3)#Lee los tres primeros
print(datos)
datos = fichero.read(4)#Lee los cuatro siguientes
print(datos)
fichero.seek(0)#Posicionando el punto de inicio de lectura en el carácter 0
datos = fichero.read(3)
print(datos)
fichero.close()

fichero = open("datos.txt", encoding="utf-8")
datos = fichero.readlines()#Guarda las lineas en una lista. Contiene los \n
#datos = [linea[:-1] for linea in datos] #Si siempre hay un \n al final
#datos = [linea.replace('\n','') for linea in datos]
#datos = list(map(lambda linea : linea.replace('\n',''), datos))
datos = [linea.strip() for linea in datos]#El método strip elimina también \n
print(datos)
fichero.close()
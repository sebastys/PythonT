#LISTA
dias_semana = ["Luns", "Martes", "Mércores", "Xoves", "Venres", "Sábado"]
dias_semana.append("Domingo")
#Acceso a un elemento
print(dias_semana[3])#Muestra "Xoves"
print(dias_semana[0])#Muestra "Luns"
#print(dias_semana[7])#IndexError
#Recorrer la lista
for dia in dias_semana:
    print(dia,end=":")
print()

#TUPLA
dias_semana = ("Luns", "Martes", "Mércores", "Xoves", "Venres", "Sábado","Domingo")
#Acceso a un elemento
print(dias_semana[3])#Muestra "Xoves"
print(dias_semana[0])#Muestra "Luns"
#print(dias_semana[7])#IndexError
#Recorrer la tupla
for dia in dias_semana:
    print(dia,end="=")
print()


#CONJUNTO
colores = {"rojo","verde","azul","rojo"}#Uno de los dos "rojos" no será aceptado
#Acceso a un elemento
#ERROR


#DICCIONARIO
diccionario = {"Lunes":"Luns",2:"Martes","Tres":"Mércores"}
#Acceso a un elemento
print(diccionario["Tres"])
#print(diccionario["Mércores"])#KeyError
#Recorrer el diccionario
for clave in diccionario.keys():
    print(clave,end="-")
print()
for valor in diccionario.values():
    print(valor,end="-")
print()
for k,v in diccionario.items():
    print(k,v,sep="=",end="*")
print()
#COPIA POR VALOR
x=5
y=x
print(y)
x=8
print(y)

#COPIA POR REFERENCIA
lista1 = [1,2]
lista2 = lista1
print(lista2)
lista1.append(3)
print(lista2)

#CREACIÓN DE DUPLICADO DE LISTA
lista1 = [1,2]
lista2 = lista1[:]
print(lista2)
lista1.append(3)
print(lista2)
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
print("ASIGNACIÓN:",lista2)#[1,2,3]

#CREACIÓN DE UNA COPIA DE UNA LISTA MEDIANTE EL MÉTODO copy
lista1 = [1,2]
lista2 = lista1.copy()
print(lista2)
lista1.append(3)
print("COPY:",lista2) #[1,2]

#CREACIÓN DE DUPLICADO DE LISTA A TRAVÉS DE UN SLICING
lista1 = [1,2]
lista2 = lista1[:]
print(lista2)
lista1.append(3)
print("SLICING:", lista2)#[1,2]
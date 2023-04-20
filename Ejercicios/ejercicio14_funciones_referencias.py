#PASO DE PARÁMETROS POR VALOR
def funcion1(a):
    a=a+1

x=10
funcion1(x)
print(x)#10

#PASO DE PARÁMETRO POR REFERENCIA
def funcion2(b):
    b.append(5)

y=[1,3]
funcion2(y)
print(y)#[1,3,5]

#PASO DE PARÁMETRO POR VALOR DE UNA LISTA
def funcion2(b):
    b.append(5)

y=[1,3]
funcion2(y.copy())
print(y)#[1,3]
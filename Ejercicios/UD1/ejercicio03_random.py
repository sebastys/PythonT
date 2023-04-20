import random
from dias import dias_semana

#Función seed()
random.seed()#Genera una semilla basada en el reloj
#random.seed(10)#Genera una semilla a partir de un valor. La secuencia será siempre la misma.
print(random.random())#Genera un número en el segmento [0,1)
print(random.random())#Genera un número en el segmento [0,1)
print(random.randint(1,6))#Genera un aleatorio en el segmento [x,y]
print(random.choice(dias_semana))#Elige un elemento al azar de la lista/tupla
print(random.choices(dias_semana,k=3))#Selecciona un subconjunto al azar del la lista/tupla
print(random.sample(dias_semana,k=3))#Selecciona un subconjunto NO REPETIDO al azar del la lista/tupla
print(random.randrange(10))#Elige al azar entre 0 y n-1 (9 en el ejemplo)
print(random.randrange(5,10))#Elige al azar entre 5 y n-1 (9 en el ejemplo)
print(random.randrange(0,10,3))#Elige un número entre 0,3,6 y 9 (en el ejemplo)
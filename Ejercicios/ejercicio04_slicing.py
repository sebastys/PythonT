bichejos = ["gato.png","perro.jpg","gallina.gif"]

#Crear una nueva lista con los nombres de los ficheros 
#sin las extensiones
animales = [] #Creación de una nueva lista vacía
#animales = list() #Creación de una nueva lista vacía
for bichejo in bichejos:
    bichejo_sin_extension = bichejo[:-4]
    animales.append(bichejo_sin_extension)

print(animales)
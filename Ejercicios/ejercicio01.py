nombre = input("Introduce tu nombre:")
print("Hola, te llamas",nombre)
#El parámetro sep indica qué separador utilizar cuando hay comas
print("Hola, te llamas",nombre,sep="****-****")#Un comentario
'''
Comentario 1
Comentario 2
Comentario 3
'''
nombre1="Francisco"
nombre2="Santi"
nombre3="José Manuel"
#Asignación equivalente:
nombre1, nombre2, nombre3="Fran","Santi","José Manuel"
#El parámetro end modifica el salto de línea por lo que indiquemos
print(nombre1,end="---")
print(nombre2,end="***")
print(nombre3)

#f-string
nombre="Fernando"
altura=170
print(f"La persona con el nombre {nombre} y altura {altura} me está mirando")

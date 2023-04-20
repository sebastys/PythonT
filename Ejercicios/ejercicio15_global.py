def funcion():
    global x
    global y #Declara a nivel global una variable
    x=x+1
    print(x)
    y=15 #Inicializa la variable global y

x=10
funcion()
print(y) #Muestra el valor de la variable global y creada en la función
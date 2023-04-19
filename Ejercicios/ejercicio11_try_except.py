def dividir(d1, d2):
    lista=[3,8,4]
    #lista[4]#IndexError si el índice no existe
    diccionario = {1:"Uno",3:"Tres",8:"Ocho"}
    #diccionario[4]#KeyError si la clave no existe
    resultado = d1/d2 #ZeroDivisionError
    return resultado

try:
    r = dividir(5,0)
    print(r)
except ZeroDivisionError as zde:
    print("No puedes dividir entre cero")
except (IndexError, KeyError):#IndexError o KeyError
    print("Ha ocurrido un error de acceso a un elemento de la colección")
else:
    print("Ha ido bien")
finally:
    print("El bloque finally es opcional")
    print("El bloque finally siempre se ejecuta")


'''
try:
    r = dividir(5,0)
except IndexError as alcanfor:
    print(alcanfor)
except BaseException as be:
    print(be)
'''



'''
try:
    r = dividir(5,0)
    print(r)
except ZeroDivisionError:
    print("Error de zero")
except ArithmeticError:
    print("Error aritmético")
except IndexError:
    print("Error de índice")
except:
    print("Error desconocido")
'''
    

'''
try:
    r = dividir(5,2)
    print(r)
except:
    print("Error")
'''



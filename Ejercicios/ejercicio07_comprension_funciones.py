def censurar(palabra : str) -> str:
    palabras_prohibidas = ("mameluco","sable","lavadora")
    if palabra.lower() in palabras_prohibidas:
        return("***")
    else:
        return palabra

texto = '''
El Mameluco llegó en su automóvil
y sentí un flechazo al momento y me compré una lavadora
'''
lista = texto.split()

nueva_lista = [censurar(palabra) for palabra in lista]
nuevo_texto = " ".join(nueva_lista)
print(nuevo_texto)



'''
def sumar(s1 : int, s2 : int) -> int:
    resultado = s1 + s2
    return resultado
'''



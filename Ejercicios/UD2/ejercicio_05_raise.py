#s1 no puede ser igual a s2
#s1 y s2 deben ser enteros
def sumar(s1 : int, s2 : int) -> int:
    s1_no_es_entero = not isinstance(s1,int)
    s2_no_es_entero = not isinstance(s2,int)
    if s1_no_es_entero or s2_no_es_entero:
        raise TypeError("Los parámetros deben ser enteros")
    if s1==s2:
        raise ValueError("Los parámetros no pueden ser iguales")

try:
    resultado = sumar(3,3)
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
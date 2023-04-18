def sumar(s1 : int, s2 : int) -> int:
    if not isinstance(s1, int) or not isinstance(s2, int):
        return "Eres un rebelde"
    resultado = s1 + s2
    return resultado

resultado = sumar("Fran", "5.2")
print(resultado)
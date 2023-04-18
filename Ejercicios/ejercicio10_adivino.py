import random

numero_secreto = random.randint(0,9)
numero_candidato=-1
contador=0
while numero_secreto!=numero_candidato:
    numero_candidato = int(input("Introduce el número candidato:"))
    contador+=1
    if numero_secreto==numero_candidato:
        print(f"Eres un adivino y has necesitado {contador} intentos")
    else:
        print("Error")



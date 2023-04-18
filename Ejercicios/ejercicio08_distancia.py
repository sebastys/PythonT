from Levenshtein import distance

palabra1 = "perro"
palabra2 = "gato"
distancia = distance(palabra1, palabra2)
print(distancia)

dias_semana = ("Luns", "Martes", "Mércores", "Xoves", "Venres", "Sábado", "Domingo")
dia = input("Introduce un día de la semana:")

if dia.capitalize() in dias_semana:
    print("Ok")
else:
    #distancia = [(5,"Luns"),(3,"Martes"),(8,"Mércores")]
    distancias = [(distance(dia_actual, dia),dia_actual) for dia_actual in dias_semana]
    print(f"Puede que quieras decir {min(distancias)[1]}")
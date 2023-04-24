lista = [3,8,1,10,-5,7]
lista_texto =["Zaragoza","Murcia","Albacete","Soria"]
#Función sorted - Proporciona una copia
lista_modificada = sorted(lista)
print(lista_modificada)
lista_modificada = sorted(lista, reverse=True)
print(lista_modificada)

lista_modificada = sorted(lista_texto)
print(lista_modificada)

#Método sort - Modifica la original
lista.sort()
print(lista)

#Uso 'avanzado' de sort y de sorted

#(Nombre de la ciudad, precio piso de 100 metros, calidad_tapas)
ciudades = [
    ("A Coruña",200_000,5),
    ("Lugo",240_000,10),
    ("Ourense",135_000,7),
    ("Pontevedra",210_000,0)
]

def ponderacion_rebeca(ciudad):
    return ciudad[1]

def ponderacion_sebastian(ciudad):
    print("PONDERANDO...")
    return ciudad[2]

ciudades_preferidas_rebeca = sorted(ciudades, key=ponderacion_rebeca)
print("Ciudades Rebeca:", ciudades_preferidas_rebeca)

ciudades.sort(key=ponderacion_sebastian, reverse=True)
print("Ciudades Sebastian:", ciudades)
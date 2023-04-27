import time

alergenos = ['pulpo','sepia','bacalao']

#función filter
def is_cefalopodo(bicho) -> bool:
    cefalopodos = ['calamar','sepia','pulpo']
    return bicho in cefalopodos

alergenos_cefalopodos = filter(is_cefalopodo, alergenos)
alergenos_cefalopodos = list(alergenos_cefalopodos)
print(alergenos_cefalopodos)

#función map
def convertir_mayusculas(nombre : str) -> str:
    print("Convirtiendo...")
    return nombre.upper()

alergenos_mayusculas = map(convertir_mayusculas, alergenos)

#Hasta que no se itera por el alergenos_mayusculas(objeto map) no se aplica la función
for am in alergenos_mayusculas:
    print(am)
    time.sleep(5)
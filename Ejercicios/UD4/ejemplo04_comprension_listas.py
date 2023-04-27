alergenos = ['pulpo','sepia','bacalao']
#Lista con todos los alérgenos
lista_alergenos = [al for al in alergenos]
print(lista_alergenos)

#Lista con las primeras tres letras de los alérgenos
lista_alergenos = [al[:3] for al in alergenos]
print(lista_alergenos)

#Lista con los alérgenos que contengan la letra p
lista_alergenos = [al for al in alergenos if 'p' in al]
print(lista_alergenos)

#Lista con los alérgenos que contengan la letra p convertidos a mayúsuculas y el 
#resto a capitalize
lista_alergenos = [al.upper() if "p" in al else al.capitalize() for al in alergenos]    
print(lista_alergenos)
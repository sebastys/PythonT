f1 = lambda : 2
print(f1())
f2 = lambda x : x*2
print(f2(8))
f3 = lambda x,y : x+y
print(f3(3,4))

alergenos = ['pulpo','langostinos','bacalao',"rape","ajo"]
alergenos_mas_4 = filter(lambda nombre : len(nombre)>4, alergenos)
print(list(alergenos_mas_4))


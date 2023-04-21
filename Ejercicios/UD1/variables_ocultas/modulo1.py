#Con este import, _f2 y __f3 son privados
'''
from modulo2 import *
f1()
_f2()
__f3()
'''
#Con este import, _f2 y __f3 son accesibles.
import modulo2
modulo2.f1()
modulo2._f2()
modulo2.__f3()
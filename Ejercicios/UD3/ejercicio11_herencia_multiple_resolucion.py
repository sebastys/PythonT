class A:
    def x(self):
        return "A"

class B(A):
    def x(self):
        return "B"

class C(A):
    def x(self):
        return "C"

class D(B,C):
    def x(self):
        return "D"

d = D()
print(d.x())
print(D.mro())


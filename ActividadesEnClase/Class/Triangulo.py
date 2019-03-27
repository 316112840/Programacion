
import random as r
from math import fabs

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def __str__ (self):
        return "Triangulo de lados: " + str(self.a) + " " + str(self.b) + " " + str(self.c)




def TrianguloAleatorio():
    a = r.uniform(0, 10)
    b = r.uniform(0,10)
    c = r.uniform( fabs(a-b), a + b)
    return Triangulo(a, b, c)
        
print(TrianguloAleatorio())

# -*- coding: utf-8 -*-
# Mariana Yasmin Martinez Garcia
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 5.2: Ejercicio para dos puntos extra sobre la tarea
import random as r
from MatrizLista import *


class MatrizNN:

    def __init__ (self, N, matriz):
        self.n = N
        self.matriz = matriz



    def __str__(self):
        cadena = ""
        for i in self.matriz:
            cadena =  cadena + str(i) + "\n"
        return cadena



    def __matmul__(matriz1, matriz2):
        a, b, c, m = matriz1.n, matriz1.matriz, matriz2.matriz, []
        for i in range(a):
            for j in range(a):
                m.append(b[i][j] * c[j][i])
        z = MatrizLista(a, m)
        return z




# PRUEBAS:

m1 = MatrizNN(2, [[1,2],[3,4]])
m2 = MatrizNN(2, [[5,6],[7,8]])
print(m1)
print(m2)

m3 = m1@m2
print(m3)

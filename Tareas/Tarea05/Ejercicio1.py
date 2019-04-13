# -*- coding: utf-8 -*-
# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 5.1: Clase MatrizNN parte 1
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



    def cerosNN(N):
        l = []
        m = []
        for i in range(N):
            l.append(0)
            m.append(l)
        return MatrizNN(N, m)



    def identidadNN(N):
        m = []
        for i in range(N):
            fila = [0 for i in range(N)]
            m.append(fila)
            m[i][i] = 1
        return MatrizNN(N, m)



    def aleatoriaNN(N):
        m = []
        for i in range(N):
            m.append([r.randrange(-9 ,9) for i in range(N)])
        return MatrizNN(N, m)



    def __add__(matriz1, matriz2):
        
        if matriz1.n == matriz2.n:
            l = []
            for i in range(matriz1.n):
                for j in range(matriz1.n):
                    l.append(matriz1.matriz[i][j] + matriz2.matriz[i][j] )
            matriz = MatrizLista(matriz1.n , l)
            return MatrizNN(matriz1.n , matriz)

        else:
            print("ERROR. La longitud de las matrices debe ser la misma.")



    def __sub__(matriz1, matriz2):
        
        if matriz1.n == matriz2.n:
            l = []
            for i in range(matriz1.n):
                for j in range(matriz1.n):
                    l.append(matriz1.matriz[i][j] - matriz2.matriz[i][j] )
            matriz = MatrizLista(matriz1.n , l)
            return MatrizNN(matriz1.n , matriz)

        else:
            print("ERROR. La longitud de las matrices debe ser la misma.")



    def __mul__(matriz, escalar):
        l = []
        for i in range(matriz.n):
            for j in range(matriz.n):
                l.append(matriz.matriz[i][j] * escalar)
        m = MatrizLista(matriz.n , l)
        return MatrizNN(matriz.n , m)
        
                    
        
        




# Pruebas:

m1 = MatrizNN(3, [[1,2,3],[4,5,6],[7,8,9]])
print(m1)

m2 = MatrizNN.cerosNN(4)
print(m2)

m3 = MatrizNN.identidadNN(5)
print(m3)

m4 = MatrizNN.aleatoriaNN(4)
print(m4)

m5 = MatrizNN(3, [[1,4,5],[1,6,7], [8,4,1]])
m6 = m1 + m5
print(m6)

m7 = m1 - m5
print(m7)

m8 = m1 * 2
print(m8)

m9 = m1 + m2
m10 = m1 - m2
            
        

        
    

# -*- coding: utf-8 -*-
# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
''' Este es un metodo que se hizo en clase.
El metodo recibe un numero entero N y una lista de numeros, y crea una matriz de longitud N
con los numeros de la lista.'''


def MatrizLista(N, lista):
        l = []
        for i in range(N):
            m = []
            for j in range(N):
                m.append(lista[i*N + j])
            l.append(m)
        return l 




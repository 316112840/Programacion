# -*- coding: utf-8 -*-
# Mariana Yasmin Martinez Garcia
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 7.1: Practica con sets


def InterseccionConjuntos(lista):
    a = lista[0]
    
    for i in range( len(lista) ):
        a =  a.intersection( lista[i] )

    return a
            








# PRUEBAS:
a = set()
b = set()
c = set()
d = set()
for i in range(10):
    a.add(i)
    
for i in range(8):
    b.add(i*2)
    
for i in range(15):
    if i%2 != 0:
        c.add(i)
        
for i in range(2,10):
    d.add(i)

print(a, "\n", b, "\n", c , "\n", d, "\n" )



        
e = InterseccionConjuntos([ a, b, c, d ])
print( e, "\n" )

f = InterseccionConjuntos([ a, b, d])
print( f, "\n" )


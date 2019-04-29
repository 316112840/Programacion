# -*- coding: utf-8 -*-
# Mariana Yasmin Martinez Garcia
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 6.1: Práctica con diccionarios.
import random as r


# A)

a = [r.randint(-10000, 10000) for i in range(100)]

Diccionario = { i : True if i%2==0 else False  for i in a }

print(Diccionario, "\n")






# B)

def CeroNegPos(i):
    if i == 0:
        x= "Cero"
    elif i < 0:
        x = "Negativo"
    elif i>0:
        x = "Positivo"
    return x


b = [r.uniform(-1000,1000) for i in range(100)]

#Diccionario2 = { i : "Negativo" if i<0 else"Positivo" for i in b}    <====Aqui es donde quiero poner la otra condicional para cuando i sea igual a 0.
        
Diccionario2 = { i: CeroNegPos(i) for i in b}

print(Diccionario2, "\n" )






# C)

ABC = "ABCDEFGHIJKLMNOPQRSTUVWQYZ"
abc = "abcdefghijklmnopqrstuvwxyz"

Diccionario3 = { ABC[i] : abc[i] for i in range(26) }

print(Diccionario3, "\n")






# D)

def CadenaPseudoaleatoria(Longitud):
    aA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQYZ"
    cad = ""
    for i in range(Longitud):
        cad += aA[r.randint(0,41)] 
    return cad


d = [ CadenaPseudoaleatoria(r.randint(0,50)) for i in range(100)]

Diccionario4 = { j : len(j) for j in d}

print(Diccionario4, "\n")






# E)

Diccionario5 = { "H" : "Hidrogeno", "He": "Helio", "Li": "Litio", "Be": "Berilio", "B": "Boro", "C":"Carbono", "N": "Nitrogeno", "O":"Oxigeno", "F":"Fluor", "Ne": "Neon"}

print(Diccionario5, "\n")







# F)

def ListaN(N):
    L = [1]
    for i in range(N - 1):
        L.append( L[len(L) - 1] + 1 )
    return L


Diccionario6 = { i : ListaN(i) for i in range(1,21)}

print(Diccionario6)

''' Esto es lo qu se hizo la clase del viernes 5 de abril.
La primer parte es lo que estabamos viendo la clase anterior.
Posteriormente, usamos el operador ternario e hicimos varios ejemplos
usandolo.
'''

import random as r


def Identidad(N):
    matriz = []

    for i in range(N):
        fila = [0 for i in range(N)]
        matriz.append(fila)

    for i in range(N):
        matriz[i][i] = 1

    return matriz


# Esta es una forma de imprimir las matrices:
m = Identidad(5)
for i in m:
    print(i)

print("\n")

# Esta es otra forma:
for i in range(5):
    print(m[i])

print("\n")





# El operador ternario: Nos permitirá usar un if de una manera mas abreviada.
# Sintaxis: variable = valor1 if valor2

# Ejemplo:

val1 = 3
val2 = 5
var = val1 if val1 > val2 else val2
print(var, "\n")

# Otro ejemplo:

l = []
for i in range(20):
    l.append(r.randint(1,5)) # Con esto se creo una lista con 20 numeros aleatorios del 1 al 5.

# Estas tres formas colocaran un True si es par, y False si es impar.
lista = []
for i in range(20):
    valor = True if l[i]%2 == 1 else False
    lista.append(valor) 
print(lista, "\n")

# Forma 2: 
lista1 = [ True if l[i]%2 == 1 else False for i in range(20) ]
print(lista1, "\n")

# Forma 3: 
lista2 = [True if i%2 == 1 else False for i in l ]
print(lista2, "\n" )



# Ahora haremos la funcion Identidad usando el operador ternario.

def IdentidadN(N):
    matriz = [[1 if i == j else 0 for i in range(N) ] for j in range(N) ]
    return matriz


print(IdentidadN(4), "\n")



def Triangular(N):
    matriz = [[1 if i > j else 0 for i in range(N) ] for j in range(N) ]
    return matriz

print(Triangular(4))


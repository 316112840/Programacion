# set

s = set()
for i in range(1,11):
    s.add(i)

s.add(10) # Si hay varios elementos repetidos, solo tomara uno de ellos. No se repetiran.

s1 = set()
for i in range(8, 15):
    s1.add(i)

print(s)


# Union
s2 = s | s1
print(s2)


# Diferencia
s3 =  s - s1
print(s3)


# Interseccion
print(s.intersection(s1))


# Diferencia simetrica
print(s1.symmetric_difference(s), "\n")





''' Programar un metodo que reciba una lista de numeros y determine cuantos numeros distintos pueden obtenerse como
una suma de dos elementos diferentes de la lista. Y que imprima la lista de numeros posibles.'''
def sumaL(L):
    q = set()
    for i in L:
        for j in L:
            if i != j:
                q.add(i + j)
    print("Posibles numeros: " , q, "\nCantidad de numeros: ", len(q), "\n")


sumaL([5,2,3,4])



# Otra forma de escribir el metodo anterior por listas por comprension:
def sumaLista(L):
    n = len(L)
    l = [ L[i] + L[j] for i in range(n) for j in range(i +1, n)]
    NumerosPosibles = set(l)
    print("Numeos posibles: ", NumerosPosibles, "\nCantidad de numeros: ", len(NumerosPosibles))

sumaLista([5,2,3,4])


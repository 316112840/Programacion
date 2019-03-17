# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 2.3: Práctica con el módulo math.

from math import *

# a)
def SumaEntera(L):
    '''Sumará la parte entera de los números de la lista dada'''
    N = [0]
    for numero in L:
        N.append(floor(numero) + N[len(N)-1])
    return N[len(N)-1]


# b)
def SinCosTan( GradRad, Angulo):
    ''' Escribir "Radianes" seguido del ángulo si éste está en radianes.
        Escribir "Grados" seguido del ángulo si éste está en grados.'''
    if GradRad == "Radianes":
        print( "Seno del angulo dado:", sin(Angulo), "\nCoseno del angulo dado:", cos(Angulo), "\nTangente del angulo dado:", tan(Angulo))
    if GradRad == "Grados":
        seno = sin( radians(Angulo))
        coseno = cos( radians(Angulo))
        tangente = tan( radians(Angulo))
        print( "Seno del angulo dado:", seno, "\nCoseno del angulo dado:", coseno, "\nTangente del angulo dado:", tangente)


# c)
def CosLognValor(numero):
    return cos(log(fabs(numero), e ))


# d)
def LognDelProducto(L):
    N = [1]
    for i in range( len(L)):
        N.append( L[i] * N[len(N)-1])
    return log(fabs(N[len(N)-1]), e)





# Pruebas:
S = "   "
# a)
print(SumaEntera([5.2, 45.3, 3.4]))
print(S)
print(S)

# b)
SinCosTan("Radianes", pi/2 )
print(S)
SinCosTan("Grados", 90)

# c)
print(S)
print(CosLognValor(42.6))
print(CosLognValor(-42.6))

# d)
print(S)
print(LognDelProducto([1.2,1.1,1.3]))

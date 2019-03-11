# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 2.1: Setters y getters

class VectorND:
    def __init__(self,n,l):
        self.__n = n
        self.__l = l
        
    # Getters:
    def getL(self, N):
        ''' Ingrese un valor N. Este corresponderá al número de
            la posición de la entrada del vector que desea conocer '''
        if 0 < N <= self.__n :
            return (self.__l[N - 1])
        else:
            y = "ERROR. La posición ",N, "no existe en el vector que ingresó."
            return y 

    def getN(self):
        return self.__n

    # Setters:
    def setL(self, Posicion, ValorNuevoL):
        self.__l[Posicion -1] = ValorNuevoL
        

    def imprimir(self):
        for i in range(self.__n):
            print(self.__l[i])
            
    def multiplicacion(self,c):
        for i in range(self.__n):
            self.__l[i] = self.__l[i] * c
            
    def suma(v1,v2):
        if v1.__n == v2.__n:
            L = []
            for i in range(v1.__n):
                    L.append(v1.__l[i]+v2.__l[i])
            return VectorND(v1.__n, L)
        else:
            print("La dimension de los vectores no coincide.")


V1 = VectorND(4, [71,32,54,98])
V1.imprimir()
print("El valor correspondiente a la posicion 2 del vector dado es:", V1.getL(2))
print( "La cantidad de entradas que contiene el vector dado es:",V1.getN())

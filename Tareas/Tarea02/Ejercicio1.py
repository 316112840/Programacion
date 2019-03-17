# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 2.1: Setters y getters
# A)

class VectorND:
    def __init__(self,n,l):
        self.__n = n
        self.__l = l
        
    # Getters:
    def getPosicionEnL(self, N):
        ''' Ingrese un valor N. Este corresponderá al número de
            la posición de la entrada del vector que desea conocer '''
        if 0 < N <= self.__n :
            return (self.__l[N - 1])
        else:
            y = "ERROR. La posición ",N, "no existe en el vector que ingresó."
            return y 

    def getN(self):
        return self.__n

    def getL(self):
        return self.__l


    # Setters:
    def setPosicionEnL(self, Posicion, ValorNuevoL):
        ''' Ingresar un Posicion y el valor nuevo que quiere que tome esa posicion.'''
        self.__l[Posicion -1] = ValorNuevoL

    def setN(self, NuevoValorN, EntradasNuevas):
        ''' Ingresar el nuevo valor correspondiente a las entradas que tendrá el
            vector, y también el valor de estas nuevas entradas en forma de lista.
            Estas nuevas entradas se colocarán después de las entradas del vector
            original. '''
        for i in EntradasNuevas:
            self.__l.append(i)

    def setL(self, EntradasNuevas):
        ''' Ingresar el valor de las entradas nuevas en forma de lista.
            Si la longitud del vector no coincide con la longitud de las entradas
            nuevas, ese valor se cambiará. '''
        self.__l = EntradasNuevas
        self.__n = len(EntradasNuevas)

            
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


# Pruebas:
S = "   "

V1 = VectorND(4, [71,32,54,98])
print("El valor correspondiente a la posicion 2 del vector dado es:", V1.getPosicionEnL(2))
print( "La cantidad de entradas que contiene el vector dado es:",V1.getN())
print("Y sus entradas son: ", V1.getL() )

print(S)
V2 = VectorND(3, [12, 56, 7])
V2.setPosicionEnL(2,45)
print("El nuevo valor de la posicion 2 del vector V2 será 45: ",V2.getL())

print(S)
V3 =  VectorND(4, [1,2,3,4])
V3.setN(6, [5,6])
print("El vector V3 tendrá ahora 6 entradas y los valores que se añadirán son [5,6]: ",V3.getL())

print(S)
V4 = VectorND(4, [12, 23, 34, 45])
V4.setL([65,71,3])
print( "Las nuevas entradas del vector V4 son: ",V4.getL(), "\nY el valor correspondiente a su longitud es:", V4.getN())

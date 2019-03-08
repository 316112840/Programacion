class Vector3d:
    def __init__(self,x,y,z):
        self.__x = x # Para colocar un atributo privado basta colocar "__" (dos guiones bajos) al inicio, por ejemplo:
        self.__y = y
        self.__z = z
    def __add__(a,b): # Sobrecarga de operadores
        return Vector3d(a.__x + b.__x, a.__y + b.__y, a.__z + b.__z )
    def __sub__(a,b): # Sobrecarga de operadores
        return Vector3d(a.__x - b.__x, a.__y - b.__y, a.__z - b.__z )
    #def __mul__(a,b):
        #Falta terminar este 
    def imprime(self):
        print("x:",self.__x, "\ny:", self.__y, "\nz:", self.__z )     
# getX servirá para mostrar el valor de X, y setX servirá para cambiar el valor de X
    # Getters:
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    # Setters:
    def setX(self,Xnuevo):
        self.x = Xnuevo
    def setY(self, Ynuevo):
        self.y = Ynuevo
    def setZ(self, Znuevo):
        self.z = Znuevo

# Y para poder acceder a los atributos privados, se usará "self.__x" si es dentro de la clase.
# Si es fuera de la clase se usará "__Vector3d__x"


# Encapsulación. 
# Atributo privado (solo se puede acceder a ellos mediante métodos de la misma clase) y atributo público (hasta ahorita habíamos usado de estos últimos)
# En python no hay atributos verdaderamente privados, siempre se podrá acceder a ellos de alguna manera.


    

# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 2.2: Sobrecarga de operadores.


class VectorND:
    def __init__(self,n,l):
        self.n = n
        self.l = l

    def imprimir(self):
        for i in range(self.n):
            print(self.l[i])
            
    def __mul__(self,c):
        for i in range(self.n):
            self.l[i] = self.l[i] * c

    def __add__(v1,v2):
        if v1.n == v2.n:
            L = []
            for i in range(v1.n):
                L.append(v1.l[i] + v2.l[i])
            return VectorND(v1.n,L)
        else:
            print("La dimension de los vectores no coincide.")

    def __sub__(v1,v2):
        if v1.n == v2.n:
            L = []
            for i in range(v1.n):
                L.append(v1.l[i] - v2.l[i])
            return VectorND(v1.n,L)
        else:
            print("La dimension de los vectores no coincide.")


# Pruebas: 
v1 = VectorND(4, [1,2,3,4])
v2 = VectorND(4, [9,8,7,6])
v3 = VectorND(5, [2,5,6,9,12])
v4 = v1 + v2
v5 = v2 - v1
v3 * 2
print("Entradas del vector 1: ", v1.l)
print("Entradas del vector 2: ", v2.l)
print("Estas son las entradas del vector que resulto de la suma de los dos vectores anteriores: ",v4.l)
print("Estas son las entradas del vector que resulto de la resta de los dos vectores anteriores(v2 - v1): ",v5.l)
print("Estas son las entradas del vector v3 por 2: ", v3.l)

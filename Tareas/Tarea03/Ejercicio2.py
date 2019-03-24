# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 3.2: Ejercicio para dos puntos extra sobre la tarea
from random import *

class ListaDeNumeros:
    def __init__ (self, lista, n):
        self.lista = lista
        self.n = n

    def Agregar(self, NuevoNumero):
        self.lista.append(NuevoNumero)
        self.n += 1
        
    def AgregarAleatorio(self):
        self.lista.append(random())
        self.n += 1

    def Eliminar(self):
        self.lista.pop()
        self.n = self.n - 1

    def Pares(self):
        pares = 0
        for i in self.lista:
            if i%2 == 0:
                pares += 1
        return pares

    def Impares(self):
        impares = 0
        for i in self.lista:
            if i%2 != 0:
                impares += 1
        return impares

# Pruebas:
S = "\n"

A = ListaDeNumeros([1,2, 3,4,5,6,7,8,9,10], 10)
print( A.lista, "\nCANTIDAD DE ELEMENTOS EN LA LISTA: ", A.n , S)


A.Agregar(11)
print(A.lista, "\nCANTIDAD DE ELEMENTOS EN LA LISTA: ", A.n ,S)


A.AgregarAleatorio()
print(A.lista, "\nCANTIDAD DE ELEMENTOS EN LA LISTA:", A.n, S)


A.Eliminar()
print(A.lista, "\nCANTIDAD DE ELEMENTOS EN LA LISTA:", A.n, S)

print("CANTIDAD DE NUMEROS PARES: ", A.Pares())
print("CANTIDAD DE NUMEROS IMPARES: ",A.Impares())

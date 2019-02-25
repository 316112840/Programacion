# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 1.2: Clase Parábola

class VectorND:
    def __init__(self, n, V):
        self.n = n
        self.V = V
    def MostrarEntradas(self):
        if self.n == len(self.V):
            print("Las entradas del Vector dado son: ")
            for i in range(self.n):
                print(self.V[i] )
        else :
            print("ERROR. El valor", self.n,"no corresponde con la cantidad de elementos que contiene el vector.")
    def MultiplicarPorEscalar(self, c):
        Vector3 = []
        if self.n == len(self.V):
            for i in range(self.n):
                Vector3.append(self.V[i]*c)
            print("El vector que resulta de multilicar el vector ingresado por",c,"es:",Vector3)
        else :
            print("ERROR. El valor", self.n,"no corresponde con la cantidad de elementos que contiene el vector.")
    def SumaDeVectores(Vector1,Vector2):
        Vector4 = []
        if Vector1.n == len(Vector1.V) and Vector2.n == len(Vector2.V):
            if Vector1.n == Vector2.n:
                for i in range(Vector1.n):
                    Vector4.append(Vector1.V[i] + Vector2.V[i])
                print("El vector que resulta de sumar los dos vectores dados es: ", Vector4 )
            else:
                print("ERROR. Ambos vectores debe tener la misma cantidad de elementos para poder sumarlos.")
        else:
            print("ERROR. El valor de n de alguno de los vectores dados, no corresponde con la cantidad de elementos que contiene el vector.")
                
            

S = "                       "
V1 = VectorND(5, [9,2,3,4,5])
V2 = VectorND(6, [1,4,7,9,12,8])
V3 = VectorND(5, [4,6,8,13,5])
V4 = VectorND(3, [1,2,3,4])
V1.MostrarEntradas()
print(S)
V1.MultiplicarPorEscalar(3)
print(S)
V1.MultiplicarPorEscalar(5)
print(S)
VectorND.SumaDeVectores(V1,V2)
print(S)
VectorND.SumaDeVectores(V1,V3)
print(S)
V4.MostrarEntradas()
        

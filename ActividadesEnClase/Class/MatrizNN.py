class MatrizNN:

    def __init__(self, N, matriz):
        self.n = N
        self.matriz = matriz



    def mostrarMatriz(self):
        for i in self.matriz:
            print(i)



    def MatrizLista(N, lista):
        l = []
        
        indice = 0
        
        for i in range(N):
            m = []
            for j in range(N):
                m.append(lista[indice])
                indice += 1
            l.append(m)
        return MatrizNN(N, l)



    # Otra forma de escribir el metodo anterior es:
    def MatrizLista2(N, lista):
        l = []
        for i in range(N):
            m = []
            for j in range(N):
                m.append(lista[i*N + j])
            l.append(m)
        return MatrizNN(N, l)



    # Otra forma:
    def MatrizLista3(N, lista):
        m = MatrizNN.cerosNN(N) # Este es un metodo que se hara en la tarea.
        for i in range(N):
            for j in range(N):
                m.matriz[i][j] = lista[i*N + j]
        return m



    def suma1(M):
        for i in range(M,N):
            for j in range(M,N):
                M.matriz[i][j] += 1
        return M
        




# Pruebas: 
m1 = MatrizNN(3, [[1,2,3], [4,5,6],[7,8,9]])
m1.mostrarMatriz()

print("\n")

m2 = MatrizNN.MatrizLista(3, [1,2,3,4,5,6,7,8,9])
m2.mostrarMatriz()

print("\n")

m3 = MatrizNN.MatrizLista2(3, [1,2,3,4,5,6,7,8,9])
m3.mostrarMatriz()

                
print(MatrizNN.suma1(m1))

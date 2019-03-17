# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 2.1: Setters y getters
# B)


class Triangulo:
    def __init__(self,lado_a,lado_b,lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def desplegar(self):
        print("Triangulo de lados",self.lado_a,self.lado_b,self.lado_c)

    # Getters:
    def getLadoA(self):
        return self.lado_a

    def getLadoB(self):
        return self.lado_b

    def getLadoC(self):
        return self.lado_c

    def getTodosLosLados(self):
        return self.lado_a , self.lado_b, self.lado_c


    # Setters:
    def setLadoA(self, ValorNuevoA):
        if ValorNuevoA <= (self.lado_b + self.lado_c) :
            self.lado_a = ValorNuevoA
        else:
            print("ERROR. El lado A no puede tomar ese valor ya que el triangulo que formaría no existe.")

    def setLadoB(self, ValorNuevoB):
        if ValorNuevoB <= (self.lado_a + self.lado_c) :
            self.lado_b = ValorNuevoB
        else:
            print("ERROR. El lado A no puede tomar ese valor ya que el triangulo que formaría no existe.")

    def setLadoC(self, ValorNuevoC):
        if ValorNuevoC <= (self.lado_b + self.lado_a) :
            self.lado_c = ValorNuevoC
        else:
            print("ERROR. El lado A no puede tomar ese valor ya que el triangulo que formaría no existe.")

    def setTodosLosLados(self, ValorNuevoA, ValorNuevoB, ValorNuevoC):
        L = []
        L.append(ValorNuevoA)
        L.append(ValorNuevoB)
        L.append(ValorNuevoC)
        L.sort()
        if L[2] <= (L[0] + L[1]):
            self.lado_a = ValorNuevoA
            self.lado_b = ValorNuevoB
            self.lado_c = ValorNuevoC
        else:
            print("ERROR. El triangulo con esa longitud de lados no existe")
    


# Pruebas:
S = "   "
Triangulo1 = Triangulo(1 , 4 , 4)
print("Triangulo1: ")
print("Lado A:",Triangulo1.getLadoA())
print("Lado B:",Triangulo1.getLadoB())
print("Lado C:",Triangulo1.getLadoC())
print("Valor de todos los lados:", Triangulo1.getTodosLosLados() )

print(S)
print("Triangulo2:")
Triangulo2 = Triangulo( 2, 5, 3)
Triangulo2.setLadoB(8)
Triangulo2.setLadoB(4)
print("El nuevo valor del lado B será 4:",Triangulo2.getTodosLosLados())

print(S)
print("Triangulo 3:")
Triangulo3 = Triangulo(5, 3, 1)
Triangulo3.setTodosLosLados(1,1,4)
Triangulo3.setTodosLosLados(3,4,5)
print("El nuevo valor de los lados del Triangulo3 serán 3,4 y 5 :",Triangulo3.getTodosLosLados())

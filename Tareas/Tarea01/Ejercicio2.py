# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 1.2: Clase Parábola


class Parabola:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def MostrarEcuacion(self):
        print(self.A,"x^2 + ", self.B, "x + ", self.C, "= 0")
    def TipoRaiz(self):
        x = self.B**2 - 4*self.A*self.C
        x1 = (-(self.B) + x**(1/2))/ (2.0* self.A)
        x2 = (-(self.B) - x**(1/2))/ (2.0* self.A)
        if x < 0:
            print( "La parábola con los valores ingresados no contiene alguna raíz real.")
        elif x > 0:
            y = ("La parabola con los valores dados contiene ambas raices en los reales.")
            if x1 < 0:
                if  x2 < 0:
                    print (y,"Y ambas raices son negativas.")
                elif x2 > 0:
                    print (y,"Una de sus raices es potitiva y la otra es negativa.")
                elif x2 == 0 :
                    print(y, "Una de sus raices es negativa y la otra raiz es igual a 0")
            elif x1 > 0 :
                if x2> 0 :
                    print (y,"Y ambas raices son positivas.")
                elif x2 < 0:
                    print (y,"Una de sus raices es potitiva y la otra es negativa.")
                elif x2 == 0:
                    print (y, "Una de sus raices es positiva y la otra raiz es igual a 0")
            elif x1 == 0:
                if x2 == 0:
                    print (y,"Y ambas raices son iguales a 0")
                elif x2 < 0:
                    print ("Una de sus raices es negativa y la otra es igual a 0")
                elif x2 > 0:
                    print (y, "Una de sus raices es positiva y la otra raiz es igual a 0")
        elif x == 0:
            z = "La parábola con los valores ingresados tiene ambas raíces en los reales y el valor de ambas es la misma."
            if x1 > 0:
                print(z, "Además, es positiva.")
            if x1 < 0:
                print(z, "Además, es negativa.")
    def SumaParabolas(Parabola1, Parabola2):
        D = Parabola1.A + Parabola2.A
        E = Parabola1.B + Parabola2.B
        F = Parabola1.C + Parabola2.C
        Parabola3 = Parabola(D,E,F)
        print("El resultado de la suma de las parábolas ingresadas es: ",Parabola3) 
        

P1 = Parabola(-4, 4, 1)
P2 = Parabola(13,7, 1)
P3 = Parabola(1,4,4)
S = "                                       "
P1.MostrarEcuacion()
P1.TipoRaiz()
print(S)
P2.MostrarEcuacion()
P2.TipoRaiz()
print(S)
Parabola.SumaParabolas(P1,P2)
print(S)
P3.MostrarEcuacion()
P3.TipoRaiz()



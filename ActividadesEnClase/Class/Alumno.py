import random as r

class Alumno:

    def __init__(self, numeroCuenta, nombre, promedio):
        self.numeroCuenta = numeroCuenta
        self.nombre = nombre
        self.promedio = promedio


    def __str__(self):
        cadena = "Numero: " + str(self.numeroCuenta)
        cadena += "\nNombre: " + self.nombre
        cadena += "\nPromedio: " + str(self.promedio)
        return cadena


    def listaAleatoria(n):
        l = []
        for i in range(n):
            numero = r.randint(300000000, 500000000)
            abc = "abcdefghijklmnopqrstuvwxyz"
            ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            nombre = ABC[r.randint(1,25)]
            for i in range(6):
                nombre = nombre + abc[r.randint(1,25)]
            promedio = r.uniform(5,10)
            l.append(Alumno(numero, nombre, promedio))
        return l
                         


A = Alumno.listaAleatoria(5)
for i in A:
    print(i)

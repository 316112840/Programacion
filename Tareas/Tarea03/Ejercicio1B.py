# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 3.1: Herencia
# B)
from Ejercicio1 import *

class RegistroExtendido(Herencia):
    def __init__(self, Nombre, Apellidos, NumeroDeCuenta, Calificaciones, Promedio, Faltas, Horario, Aprobado):
        super().__init__(Nombre, Apellidos, NumeroDeCuenta, Calificaciones, Promedio)
        self.faltas = Faltas
        self.horario = Horario
        self.aprobado = Aprobado

    def setHorario(self, NuevoHorario):
        self.horario = NuevoHorario

    def getHorario(self):
        return self.horario

    def AgregarFalta(self):
        self.faltas += 1

    def AgregarCalificacion(self, NuevaCalificacion):
        self.calificaciones.append(NuevaCalificacion)
        L = [0]
        for i in self.calificaciones:
            L.append( float(i) + L[len(L) -1 ])
        self.promedio = ( L[len(L) - 1] / len(self.calificaciones) )
        if NuevaCalificacion < 6:
            self.aprobado = False


# Pruebas:
print( S, "\nESTAS SON LAS PRUEBAS DE LA CLASE RegistroExtendido:")

A = RegistroExtendido( "Mariana", "Martinez", 316112840, [9,8,8,7], 8, 2, "12:00 - 21:00", True)
print(A.getHorario())

A.setHorario("13:00 - 21:00")
print(A.getHorario())

A.AgregarFalta()
print(A.faltas)

A.AgregarCalificacion(4)
print( A.promedio)
print(A.aprobado )
            

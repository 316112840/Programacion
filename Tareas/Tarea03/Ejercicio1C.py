# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 3.1: Herencia
# C)
from Ejercicio1B import *

class RegistroAnonimo(RegistroExtendido):
    def __init__(self, Nombre, Apellidos, NumeroDeCuenta, Calificaciones, Promedio, Faltas, Horario, Aprobado):
        super().__init__(Nombre, Apellidos, NumeroDeCuenta, Calificaciones, Promedio, Faltas, Horario, Aprobado)

    def __str__(self):
        cadena = "NÚMERO DE CUENTA: " + str(self.numero) +  "\nPROMEDIO: " + str(self.promedio) + "\n" + str(self.aprobado)
        return cadena


# Pruebas:

print( "\nESTAS SON LAS PRUEBAS DE LA CLASE RegistroAnonimo:")
B = RegistroAnonimo("Yasmin", "Martinez", 316112840, [8,7,8,9], 8, 4, "1:00 - 9:00", True)
print(B)

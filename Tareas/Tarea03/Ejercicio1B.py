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

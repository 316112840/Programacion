# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 3.1: Herencia
# A)

class Herencia:
    def __init__(self, Nombre, Apellidos, NumeroDeCuenta, Calificaciones, Promedio):
        self.nombre = Nombre
        self.apellidos = Apellidos
        self.numero = NumeroDeCuenta
        self.calificaciones = Calificaciones
        self.promedio = Promedio

    def __str__(self):
        cadena = "NÚMERO DE CUENTA: " + str(self.numero) + "\nNOMBRE: " + self.nombre + "\nPROMEDIO: " + str(self.promedio)
        return cadena

    def AgregarCalificacion(self, NuevaCalificacion):
        self.calificaciones.append(NuevaCalificacion)
        L = [0]
        for i in self.calificaciones:
            L.append( float(i) + L[len(L) -1 ])
        self.promedio = ( L[len(L) - 1] / len(self.calificaciones) )

    # Getters:
    def GetNombre(self):
        return self.nombre

    def GetApellidos(self):
        return self.apellidos

    def GetNumeroDeCuenta(self):
        return self.numero

    # Setters:
    def SetNombre(self, NuevoNombre):
        self.nombre = NuevoNombre

    def SetApellidos(self, NuevosApellidos):
        self.apellidos = NuevosApellidos

    def SetNumeroDeCuenta(self, NuevoNumeroDeCuenta):
        self.numero = NuevoNumeroDeCuenta


# Pruebas:
S = "\n"
Herencia1 = Herencia( "Mariana", "Martínez",31611280, [8.3,8.6,8.1,9.2], 8.55)

print(Herencia1, S)


Herencia1.AgregarCalificacion(1)

print(Herencia1.GetNombre(),S)
print(Herencia1.GetApellidos(), S)
print(Herencia1.GetNumeroDeCuenta(), S)

Herencia1.SetNombre("Yasmin")
Herencia1.SetApellidos("Martínez García")
Herencia1.SetNumeroDeCuenta(316112840)
print(Herencia1)

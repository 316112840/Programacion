import random as r

class Registro:

    numeroRegistros = 0
    
    def __ini__ (self, nombre, apellidos, edad):
        Registro.numeroRegistros += 1 # Para que cada vez que se cree un objeto, aumente una unidad
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero = Registro.numeroRegistros
        self.edad = edad


    def __str__(self):
        cadena = ""
        cadena += "Nombre: " + self.nombre + "\n"
        cadena += "Apellidos: " + self.apellidos + "\n"
        cadena += "Numero de cuenta: " + str(self.numero) + "\n"
        cadena += "Edad: " + str(self.edad)
        return cadena


    def cadenaPseudoaleatoria(n):
        abc = "abcdefghijklmnopqrstuvwxyz"
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cadena = ABC[r.randint(0,25)]
        for i in range(n - 1):
            cadena += abc[r.randint(0,25)]
        return cadena


    def RegistroPseudoaleatorio():
        nombre = Registro.cadenaPseudoaleatoria(8)
        apellidos = Registro.cadenaPseudoaleatoria(8) + " " + Registro.cadenaPseudoaleatoria(8)
        numeroCuenta= Registro.numeroRegistros
        edad = r.uniform(18,30)
        return Registro(nombre, apellidos, numeroCuenta, edad)


r1 =  Registro.RegistroPseudoaleatorio()
print(r1)

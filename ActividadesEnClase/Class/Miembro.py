# Clase base
class Miembro:

    def __init__(self, nombre, apellidos,ingreso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.ingreso = ingreso

    def __str__(self):
        return self.nombre + " " + self.apellidos

    def GetIngreso(self):
        return self.ingreso


# Clase derivada. Tendrá incluida a la clase base, más otras cosas:
class Profesor(Miembro):
    def __init__(self, nombre, apellidos, ingreso, grupos): # Tiene que contener a todos los atributos de la clase base.
        Miembro.__init__(self,nombre, apellidos, ingreso) # Se debe agregar esta línea
        self.grupos = grupos
    def GetGrupos(self):
        return self.grupos



# Clase derivada con sobrecarga de métodos:
class Alumno(Miembro):
    def __init__(self, nombre, apellidos,ingreso, grupo, matricula):
        super().__init__(nombre, apellidos, ingreso) # Esta es otra forma de llamar al constructor padre
        self.grupo = grupo
        self.matricula =  matricula

    def __str__(self): # Sobrecarga de métodos
        return str(self.nombre) + " " + self.apellidos + "\nMatricula: " + str(self.matricula)

    def GetGrupo(self):
        return self.grupo


# PRUEBAS:
A1 = Alumno("Mariana" , "Martinez Garcia", "24 de agosto del 2018", "208A", 1542)
print(A1)

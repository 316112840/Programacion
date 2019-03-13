class Boton:
    def __init__(self, Valor):
        self.Valor = Valor # El valor debe ser True o False


class Cadena:
    def __init__ (self, Cadena, NumeroEntero, Boton):
        self.__Cadena = Cadena
        self.__N = NumeroEntero
        self.__Boton = Boton
        
    # Getters:
    def GetCadena(self):
        return self.__Cadena
    def GetNumeroEntero(self):
        return self.__N
    def GetBoton(self):
        return self.__Boton

    # Setters:
    def SetCadena(self, NuevaCadena):
        if self.__Boton.Valor = True:
            self.__Cadena = NuevaCadena
    def SetNumeroEntero(self, NuevoNumeroEntero):
        if self.__Boton.Valor = True:
            if len(self.__Cadena) == NuevoNumeroEntero:
                self.__NumeroEntero = NuevoNumeroEntero
    def SetBoton(self, NuevoBoton):
        if self.__Boton.Valor = True:
            self.__Boton = NuevoBoton
    
    # Metodo para agregar un caracter al final de la cadena:
    def Agregar(self, Caracter):
        if self.__Boton.Valor = True:
            self.__Cadena += Caracter
            self.__N += 1
        
    # Metodo para eliminar el ultimo caracter de la cadena: 
    def Eliminar(self):
        if self.__Boton.Valor = True:
            self.__Cadena = self.__Cadena[0 : self.__N -2]
            self.__N -= 1
        
Boton1 = Boton(True)
Cadena1 =   Cadena("aqwert", 6, Boton1)



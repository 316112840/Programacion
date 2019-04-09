# Esta es una clase llamada Cliente.py que tendra como atributos Nombre y Valor. Y tendra como metodos Imprimir Detalles.
# Mariana Yasmin Martinez Garcia

class Cliente:
    
    def __init__ (self, Nombre, Saldo):
        self.Nombre = Nombre
        self.Saldo = Saldo

    def __str__(self):
        detalles = "NOMBRE DEL CLIENTE:" + self.Nombre + "\n" + "Saldo:" + str(self.Saldo)
        return detalles
        

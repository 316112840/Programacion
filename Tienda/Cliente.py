# Esta es una clase llamada Cliente.py que tendrá como atributos Nombre y Valor. Y tendrá como métodos Imprimir Detalles.
# Mariana Yasmin Martinez Garcia

class Cliente:
    def __init__ (self, Nombre, Saldo):
        self.Nombre = Nombre
        self.Saldo = Saldo

    def ImprimirDetalles(self):
        print("NOMBRE DEL CLIENTE: ", self.Nombre)
        print("SALDO DEL CLIENTE:", self.Saldo)
        

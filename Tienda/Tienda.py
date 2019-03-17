# Esta es una clase llamada Tienda que tiene como atributos el nombre de la tienda, un producto y un cliente.
# Y como métodos tiene imprimir detalles.
# Mariana Yasmin Martinez Garcia

from Cliente import *
from Producto import *

class Tienda:
    def __init__(self, Nombre,Cliente, Producto):
        self.Nombre = Nombre
        self.Producto = Producto
        self.Cliente = Cliente

    def __str__(self):
        detalles = "NOMBRE DE LA TIENDA: " + self.Nombre + "\n" +str(self.Cliente) +"\n" + str(self.Producto)
        return detalles

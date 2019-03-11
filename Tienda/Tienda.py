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

    def ImprimirDetalles(self):
        print( self.Nombre)
        print(self.Cliente)
        print(self.Producto)

# Esta es una clase llamada Tienda que tiene como atributos el nombre de la tienda, un producto y un cliente.
# Y como métodos tiene imprimir detalles.
# Mariana Yasmin Martinez Garcia

from Cliente import *
from Producto import *

class Tienda:
    
    def __init__(self, Nombre, Cliente):
        self.Nombre = Nombre
        self.Cliente = Cliente
        self.almacenarProductos = Tienda.almacenarProductos()


    def __str__(self):
        detalles = "NOMBRE DE LA TIENDA: " + self.Nombre + "\n" +str(self.Cliente) +"\n" 
        return detalles


    def almacenarProductos():
        productos = []
        productos.append(Producto( "Licuadora" , "Oster" , "Electrodoméstcos" , 1600.00 ))
        productos.append(Producto("Whiskas,delicias rellenas", "Whiskas","Mascotas", 54.50))
        productos.append(Producto("Aceite de coco", "San Lucas", "Despensa", 69.0))
        productos.append(Producto("Lavadora", "Whirpool", "Electrodomésticos", 3500.0))
        productos.append(Producto("Cepillo de dientes", "Colgate", "Higiene bucal", 45.0))
        for i in productos:
            print(i, "\n")

    
        


  
        



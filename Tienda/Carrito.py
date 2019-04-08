''' Esta es a clase Carrito, contiene una lista de productos de la clase Tienda.
 Y contiene cuatro metodos. Uno que agrega un producto al carrito del cliente, otro elimina un producto de su carrito,
 otro muestra los productos que contiene su carrito y el ultimo te dice el precio total de la suma de todos los
 productos de su carrito. '''
from Tienda import *


class Carrito:
    almacen = [Producto( "Licuadora" , "Oster" , "Electrodoméstcos" , 1600.00 ), Producto("Whiskas,delicias rellenas", "Whiskas","Mascotas", 54.50)]
    almacen.append(Producto("Aceite de coco", "San Lucas", "Despensa", 69.0))
    almacen.append(Producto("Lavadora", "Whirpool", "Electrodomésticos", 3500.0) )
    almacen.append(Producto("Cepillo de dientes", "Colgate", "Higiene bucal", 45.0))



    def __init__(self):
        self.carrito = []


    def agregarProducto(self,posicionProducto):
        ''' Ingrese la posicion del producto que desea añadir a su carrito. '''
        self.carrito.append(almacen[posicionProducto - 1])



    def eliminarProducto(self,posicionProducto):
        ''' Ingrese la posicion del producto que desea eliminar del carrito.  '''
        self.carrito.remove(self.carrito[posicionProducto - 1])
        


    def imprimirProductos(self):
        for producto in self.carrito:
            print( producto , "\n" )



    
            
        
        

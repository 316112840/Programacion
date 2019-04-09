''' Esta es a clase Carrito, contiene una lista de productos de la clase Tienda.
 Y contiene cuatro metodos. Uno que agrega un producto al carrito del cliente, otro elimina un producto de su carrito,
 otro muestra los productos que contiene su carrito y el ultimo te dice el precio total de la suma de todos los
 productos de su carrito. '''
from Tienda import *

class Carrito:
    
    def __init__(self, cliente):
        self.cliente = cliente
        self.carrito = []



    def agregarProducto(self,posicionProducto):
        ''' Ingrese la posicion del producto que desea añadir a su carrito. '''
        productos = Tienda.almacenarProductos()
        self.carrito.append(productos[posicionProducto - 1])



    def eliminarProducto(self,posicionProducto):
        ''' Ingrese la posicion del producto que desea eliminar del carrito.  '''
        self.carrito.remove(self.carrito[posicionProducto - 1])

        

    def mostrarTotal(self):
        almacen = Tienda.almacenarProductos()
        l = [0]
        for i in range(5):
            l.append(almacen[i].Precio + l[len(l)- 1])
        return l[len(l) - 1 ]
        


    def imprimirProductos(self):
        for producto in self.carrito:
            print( producto , "\n" )




            
        
        

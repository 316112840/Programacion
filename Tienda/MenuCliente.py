'''Esta es una clase que tiene como metodo el registro de un cliente, los datos que se ingresaran son el nombre y su saldo.
 Y se le asignará un Carrito al cliente registrado para poder agregar productos ya registrados en la clase Tienda'''

# Martinez Garcia Mariana Yasmin

from Tienda import *
from Carrito import *




class MenuCliente:


    def __init__(self):
        self.listaClientes = []




    def RegistrarCliente(self):
        
        nombre = input("Ingrese su nombre: ")
        
        saldo = input("Ingrese su saldo: ")
        
        NuevoCliente = Cliente(nombre, saldo)
        
        CarritoCliente = Carrito(NuevoCliente)

        self.listaClientes.append( [NuevoCliente, CarritoCliente] )
        
        print( "Ha sido registrado correctamente")





    def AgregarAlCarrito(self):

        print("Estos son los productos que contiene la Tienda: \n" , Tienda.mostrarProductos() )

        producto = input("Escriba la posicion del producto que desea añadir a su carrito: ")

        self.listaClientes[0][1].agregarProducto(producto)




    def eliminarDelCarrito(self):

        self.listaClientes[0][1].imprimirProductos()

        a = input("Escriba la posicion del producto que desea eliminar: ")

        self.listaClientes[0][1].eliminarProducto(a)




    def mostrarCarrito(self):

        self.listaClientes[0][1].imprimirProductos()




    def finalizarCompra(self):

        carrito = self.listaClientes[0][1]
        cliente = self.listaClientes[0][0]
        
        if carrito.mostrarTotal <= cliente.saldo:

            cliente.saldo = cliente.saldo - carrito.MostrarTotal

            print("Su compra se realizo correctamente. Vuelva pronto")
                  

        else:
                  
            print("Lo sentimos. Saldo insuficiente")
                  
        
        
        
        
        

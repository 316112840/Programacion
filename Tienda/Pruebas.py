#Esta es un clase llamada Prueba, que contendra las pruebas de las otras clases(Producto.py, Tienda.py y Cliente.py)
# Mariana Yasmin Martinez Garcia

from Carrito import *

S = "        "

class Pruebas:
    pass

    # Estas son las pruebas de la clase Producto.py :
    Producto1 = Producto( "Licuadora" , "Oster" , "Electrodomestcos" , 1600.00 )
    print(Producto1, S)
    
    Producto2 = Producto("Whiskas,delicias rellenas", "Whiskas","Mascotas", 54.50)
    print(Producto2, S)
    
    Producto3 = Producto("Aceite de coco", "San Lucas", "Despensa", 69.0)
    print(Producto3, S)
    
    Producto4 = Producto("Lavadora", "Whirpool", "Electrodomesticos", 3500.0)
    print(Producto4, S)
    
    Producto5 = Producto("Cepillo de dientes", "Colgate", "Higiene bucal", 45.0)
    print(Producto5, S)



    # Estas son las pruebas de la clase Cliente.py :
    Cliente1 = Cliente("Victoria", 1500.0 )
    print(Cliente1, S)
    
    Cliente2 = Cliente("Dante", 3670.0 )
    print(Cliente2, S)
    
    Cliente3 = Cliente("Andrea", 12380.0 )
    print(Cliente3, S)
    
    Cliente4 = Cliente("Joel", 12000.0 )
    print(Cliente4, S)
    
    Cliente5 = Cliente("Silvia", 155000.0 )
    print(Cliente5, S)
    

                       
    # Estas son las pruebas de la clase Tienda.py :
    Tienda1 = Tienda("LicuaDora's", Cliente1)
    print(Tienda1, S)
    
    Tienda2 = Tienda("Miau Miau",Cliente2)
    print(Tienda2, S)
    
    Tienda3 = Tienda("Todo de Coco",Cliente3)
    print(Tienda3, S)
    
    Tienda4 = Tienda("Lavadoras Pepe",Cliente4)
    print(Tienda4, S)
    
    Tienda5 = Tienda("La sonrisa", Cliente5)
    print(Tienda5, S, S)



    # Estas son las pruebas de la clase Carrito.py :
    carrito1 = Carrito(Cliente1)
    carrito1.agregarProducto(2)
    carrito1.agregarProducto(4)
    carrito1.agregarProducto(3)
    carrito1.eliminarProducto(3)
    carrito1.imprimirProductos()
    print("PRECIO TOTAL:", carrito1.mostrarTotal())
    

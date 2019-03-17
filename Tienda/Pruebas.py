#Esta es un clase llamada Prueba, que contendrá las pruebas de las otras clases(Producto.py, Tienda.py y Cliente.py)
# Mariana Yasmin Martinez Garcia

from Tienda import *

S = "        "

class Pruebas:
    pass

    # Estas son las pruebas de la clase Producto.py :
    Producto1 = Producto( "Licuadora" , "Oster" , "Electrodoméstcos" , 1600.00 )
    print(Producto1)
    print(S)
    
    Producto2 = Producto("Whiskas,delicias rellenas", "Whiskas","Mascotas", 54.50)
    print(Producto2)
    print(S)
    
    Producto3 = Producto("Aceite de coco", "San Lucas", "Despensa", 69.0)
    print(Producto3)
    print(S)
    
    Producto4 = Producto("Lavadora", "Whirpool", "Electrodomésticos", 3500.0)
    print(Producto4)
    print(S)
    
    Producto5 = Producto("Cepillo de dientes", "Colgate", "Higiene bucal", 45.0)
    print(Producto5)
    print(S)


    # Estas son las pruebas de la clase Cliente.py :
    Cliente1 = Cliente("Victoria", 1500.0 )
    print(Cliente1)
    print(S)
    
    Cliente2 = Cliente("Dante", 3670.0 )
    print(Cliente2)
    print(S)
    
    Cliente3 = Cliente("Andrea", 12380.0 )
    print(Cliente3)
    print(S)
    
    Cliente4 = Cliente("Joel", 12000.0 )
    print(Cliente4)
    print(S)
    
    Cliente5 = Cliente("Silvia", 155000.0 )
    print(Cliente5)
    print(S)
    
                       
    # Estas son las pruebas de la clase Tienda.py :
    Tienda1 = Tienda("LicuaDora's", Producto1, Cliente1)
    print(Tienda1)
    print(S)
    
    Tienda2 = Tienda("Miau Miau", Producto2, Cliente2)
    print(Tienda2)
    print(S)
    
    Tienda3 = Tienda("Todo de Coco", Producto3, Cliente3)
    print(Tienda3)
    print(S)
    
    Tienda4 = Tienda("Lavadoras Pepe", Producto4, Cliente4)
    print(Tienda4)
    print(S)
    
    Tienda5 = Tienda("La sonrisa", Producto5, Cliente5)
    print(Tienda5)
    print(S)

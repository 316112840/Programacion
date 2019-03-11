#Esta es un clase llamada Prueba, que contendrá las pruebas de las otras clases(Producto.py, Tienda.py y Cliente.py)
# Mariana Yasmin Martinez Garcia

from Tienda import *

S = "        "

class Pruebas:
    pass
    # Estas son las pruebas de la clase Producto.py :
    Producto1 = Producto( "Licuadora" , "Oster" , "Electrodoméstcos" , 1600.00 )
    Producto1.MostrarDetalles()
    print(S)
    Producto2 = Producto("Whiskas,delicias rellenas", "Whiskas","Mascotas", 54.50)
    Producto2.MostrarDetalles()
    print(S)
    Producto3 = Producto("Aceite de coco", "San Lucas", "Despensa", 69.0)
    Producto3.MostrarDetalles()
    print(S)
    Producto4 = Producto("Lavadora", "Whirpool", "Electrodomésticos", 3500.0)
    Producto4.MostrarDetalles()
    print(S)
    Producto5 = Producto("Cepillo de dientes", "Colgate", "Higiene bucal", 45.0)
    Producto5.MostrarDetalles()
    print(S)

    # Estas son las pruebas de la clase Cliente.py :
    Cliente1 = Cliente("Victoria", 1500.0 )
    Cliente1.ImprimirDetalles()
    print(S)
    Cliente2 = Cliente("Dante", 3670.0 )
    Cliente2.ImprimirDetalles()
    print(S)
    Cliente3 = Cliente("Andrea", 12380.0 )
    Cliente3.ImprimirDetalles()
    print(S)
    Cliente4 = Cliente("Joel", 12000.0 )
    Cliente4.ImprimirDetalles()
    print(S)
    Cliente5 = Cliente("Silvia", 155000.0 )
    Cliente5.ImprimirDetalles()
    print(S)
                       
    # Estas son las pruebas de la clase Tienda.py :
    Tienda1 = Tienda("LicuaDora's", Producto1, Cliente1)
    Tienda1.ImprimirDetalles()
    print(S)
    Tienda2 = Tienda("Miau Miau", Producto2, Cliente2)
    Tienda2.ImprimirDetalles()
    print(S)
    Tienda3 = Tienda("Todo de Coco", Producto3, Cliente3)
    Tienda3.ImprimirDetalles()
    print(S)
    Tienda4 = Tienda("Lavadoras Pepe", Producto4, Cliente4)
    Tienda4.ImprimirDetalles()
    print(S)
    Tienda5 = Tienda("La sonrisa", Producto5, Cliente5)
    Tienda5.ImprimirDetalles()
    print(S)

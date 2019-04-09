# Esta es una clase que tiene como metodo el registro de un cliente, los datos que se ingresaran son el nombre y su saldo.
# Martinez Garcia Mariana Yasmin
from Tienda import *

class MenuCliente:

    def __init__(self):
        pass


    def RegistrarCliente():
        nombre = input("Ingrese su nombre: ")
        saldo = input("Ingrese su saldo: ")
        NuevoCliente = Cliente(nombre, saldo)
        return(NuevoCliente)

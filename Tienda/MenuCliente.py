# Esta es una clase que tiene como método el registro de un cliente, los datos que se ingresarán son el nombre y su saldo.
# Martínez García Mariana Yasmin
from Tienda import *

class MenuCliente:

    def __init__(self):
        pass


    def RegistrarCliente():
        nombre = input("Ingrese su nombre: ")
        saldo = input("Ingrese su saldo: ")
        NuevoCliente = Cliente(nombre, saldo)
        return(NuevoCliente)

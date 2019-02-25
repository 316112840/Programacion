# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 1.1: Práctica de delimitación con espacios



# Programa 1: Este programa debe mostrar un mensaje con
# los primeros n números pares o impares según sea el caso
paridad = "nones" # "pares" o "nones"
n = 10 # n debe ser un entero positivo
if paridad == "pares":
    print("Los primeros",n,"números pares positivos son:")
    for i in range(1,n+1):
        print(i*2)
elif paridad == "nones":
    print("Los primeros",n,"números impares positivos son:")
    for i in range(n):
        print(i*2+1)





# Programa 2: Este programa debe declarar una clase "Auto",
# crear tres objetos y probar los tres métodos de la clase
class Auto:
    def __init__(self, marca, modelo, cantidad):
        self.marca = marca
        self.modelo = modelo
        self.cantidad = cantidad
    def mostrar(self):
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Cantidad:",self.cantidad)
    def existencia(self):
        if self.cantidad > 0:
            print("Hay",self.cantidad,"unidades en existencia.")
        else:
            print("No hay unidades en existencia.")

A_1 = Auto("Audi","A4",5)
A_2 = Auto("Mazda","CX-3",3)
A_3 = Auto("Toyota","Prius C",0)
A_1.mostrar()
A_2.existencia()
A_3.existencia()

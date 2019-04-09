'''Esta clase se llama "Producto", esta recibira el nombre de algun producto, su marca, categoria y precio.
Se modifico el metodo por "str" que nos permite facilitar la forma de llamar al objeto'''
# Martinez Garcia Mariana Yasmin

class Producto:
    
    def __init__(self, Nombre, Marca, Categoria, Precio):
        self.Nombre = Nombre
        self.Marca = Marca
        self.Categoria = Categoria
        self.Precio = Precio
        
    def __str__(self):
        detalles = "NOMBRE DEL PRODUCTO:" + self.Nombre + "\n   MARCA: " + self.Marca + "\n   CATEGORIA: " + self.Categoria + "\n   PRECIO: " + str(self.Precio)
        return detalles

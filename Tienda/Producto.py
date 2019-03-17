#Esta clase se llama "Producto", esta recibirá el nombre de algún producto, su marca, categoría y precio.
# Martinez García Mariana Yasmin

class Producto:
    
    def __init__(self, Nombre, Marca, Categoria, Precio):
        self.Nombre = Nombre
        self.Marca = Marca
        self.Categoria = Categoria
        self.Precio = Precio
        
    def __str__(self):
        detalles = "NOMBRE DEL PRODUCTO:" + self.Nombre + "\n   MARCA: " + self.Marca + "\n   CATEGORÍA: " + self.Categoria + "\n   PRECIO: " + str(self.Precio)
        return detalles

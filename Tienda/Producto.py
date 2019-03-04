#Esta clase se llama "Producto", esta recibirá el nombre de algún producto, su marca, categoría y precio.
# Martinez García Mariana Yasmin

class Producto:
    def __init__(self, Nombre, Marca, Categoria, Precio):
        self.Nombre = Nombre
        self.Marca = Marca
        self.Categoria = Categoria
        self.Precio = Precio
    def MostrarDetalles(self):
        print("NOMBRE DEL PRODUCTO: ", self.Nombre)
        print("MARCA:", self.Marca)
        print("CATEGORÍA:", self.Categoria)
        print("PRECIO: $" , self.Precio)

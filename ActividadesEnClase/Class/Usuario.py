class Usuario:
    num_de_usuarios = 0
    #metodod de inicialización:
    def __init__(self,nombre):
        Usuario.num_de_usuarios = Usuario.num_de_usuarios + 1
        self.nombre = nombre
        self.tipo_de_usuario = "cliente"
        self.clave = nombre
        print("Favor de cambiar su clave de acceso")

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Tipo de usuario:", self.tipo_de_usuario )
        print("Clave:", self.clave)


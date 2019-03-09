class Menu:
    def __init__ (self, Sopa, PlatoFuerte, Postre, Bebida):
        self.Sopa = Sopa
        self.PlatoFuerte = PlatoFuerte
        self.Postre = Postre
        self.Bebida = Bebida
    def TotalPrecio(self):
        return self.sopa.precio + self.PlatoFuerte.precio + self.Postre.Precio + self.Bebida.Precio

class Comida:
    def __init__ (self, Precio, Ingredientes):
        self.Precio = Precio
        self.Ingredientes = Ingredientes

Taco = Comida(13, ["Tortillas","Carne","Limón"])
PlatanoConCrema = Comida(25,["Platanos","Crema","Azúcar"])
Consome = Comida(35, ["Agua","Verduras","Carne"])
AguaLimon = Comida(10, ["Agua","Jugo de limon", "Azucar"])

Menu1 = Menu(Consome, Taco, PlatanoConCrema, AguaLimon)



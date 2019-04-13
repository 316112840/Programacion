
import random as r

class Agenda:

    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero


    def listaPseudo(n):
        l = []
        abc = "abcdefghijklmnopqrstuvwxyz"
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(n):
            nombre = ABC[r.randint(0,25)]
            for i in range(9):
                nombre += abc[r.randint(0,25)]
            l.append(Agenda( nombre, r.randint(1000, 1000000000)))
        return l


    def __str__ (self):
        return "NOMBRE: " +  self.nombre + "\nNUMERO: " + str(self.numero)


    def diccionario(lista):
        return{x.nombre : x.numero for x in lista}




# Pruebas:

a = Agenda("Mariana", 6156528)
print(a)

b = Agenda.listaPseudo(5)
for i in b:
    print(i, "\n")

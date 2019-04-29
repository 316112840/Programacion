# -*- coding: utf-8 -*-
# Mariana Yasmin Martinez Garcia
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 6.2: Clase Agenda
import random as r


class Agenda:

    def __init__(self, nombre, numero):
        
        self.nombre = nombre
        
        self.numero = numero





    def __str__(self):
        
        cadena = "Nombre: " + self.nombre + "\nNumero: " + str(self.numero)
        
        return cadena





    def listaPseudo(N):
        
        Lista = []
        abc = "abcdefghijklmnopqrstuvwxyz"
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for i in range(N):
            nombre = ABC[r.randint(0,25)]
            
            for i in range(9):
                nombre += abc[r.randint(0,25)]
                
            Lista.append( Agenda(nombre, r.randint(0, 100000000)) )

        return Lista





    def diccionarioNombres(Lista):

        return { n.nombre : n.numero for n in Lista }





    def diccionarioNumeros(Lista):

        return { n.numero : n.nombre for n in Lista }





    def diccionarioNombresIndices(Lista):

        return { Lista[n].nombre : n + 1 for n in range( len(Lista) )  }






# PRUEBAS

a = Agenda( "Alejandra", 65262)

print(a, "\n\n")



b = Agenda.listaPseudo(5)
for i in b:
    print(i, "\n")



c = Agenda.diccionarioNombres(b)
print(c, "\n" )



d = Agenda.diccionarioNumeros(b)
print( d, "\n" )



e = Agenda.diccionarioNombresIndices(b)
print(e)

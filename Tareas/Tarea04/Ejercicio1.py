# -*- coding: utf-8 -*-
# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 4.1: Clase Smartphone parte 1


class Smartphone:

    def __init__ (marca, pantalla, IMEI, codigoBloqueo, bloqueado, bateria):
        self.marca = marca
        self.pantalla = pantalla
        self.imei = IMEI
        self.codigo = codigoBloqueo
        self.bloqueado = bloqueado
        self.bateria = bateria


    def __str__(self):
        cadena = "MARCA: " + self.marca + "\n"
        cadena += "PANTALLA: " + str(self.pantalla) + "\n"
        cadena += "IMEI: " + self.imei + "\n"
        cadena += "CODIGO DE BLOQUEO: " + str(self.codigo) + "\n"
        cadena += "BLOQUEADO: " + self.bloqueado + "\n"
        cadena += "BATERIA: " + str(self.bateria)
        return cadena


    # Getters:
    def getCodigoBloqueo(self):
        return self.codigo


    def getBateria(self):
        return self.bateria


    # Setters:
    def setCodigoBloqueo(self, NuevoCodigo):
        self.codigo = NuevoCodigo


    def setBateria(self, ValorNuevo):
        self.bateria = ValorNuevo


    def cargaBateria(self):
        if 0 <= self.carga < 100:
            self.carga += 1


    def descargaBateria(self):
        if 0 < self.carga <= 100:
            self.carga = self.carga - 1


    def bloquear(self):
        self.bloqueado = True


    def desbloquear(self, Codigo):
        if codigo == self.codigoBloqueo:
            self.bloqueado = False
        else:
            print("ERROR. El codigo ingresado es incorrecto.")



    

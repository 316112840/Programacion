import math as m

x = m.pi
print(x, "\n")

print("{:.6}".format(x), "\n")



# Para cuando se tienen dos numeros:

y = x*x

print(" {:.5}  {:.5}    ".format(x,y), "\n")




# Para indicar cuantos numeros decimales imprimir:

print( "{:.6f}".format(x), "\n")





# Ejemplo:

''' La funcion recibira dos numeros y regresara el primer numero con la cantidad de
decimales correspondiente al segundo numero que se ingreso'''

def imprime(numero, decimales):
    cadena = "{:." + str(decimales) + "f}"
    return cadena.format(numero)




# Ejercicio (el que se envio por correo):

# a)



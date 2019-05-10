import matplotlib.pyplot as plt
import random as r
import math as m

x1 = [ i*0.01 for i in range( -1000, 1000 ) ]
y1 = [ m.cos(i) for i in x1 ]

x2 = [ i*0.01 for i in range( -1000, 1000 ) ]
y2 = [ m.sin(i) for i in x2 ]



plt.plot( x1, y1 , "b-") # la b- indica que sera linea continua azul, si fuera g-- seria una linea verde punteada.
plt.savefig( "EjemploGrafica1.png" ) # Guardara la grafica en forma de imagen con la extension .png, la extension la podemos cambiar.
plt.show()

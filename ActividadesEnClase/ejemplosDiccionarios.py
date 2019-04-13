''' Los diccionarios son otra estructura de datos que Python ya trae implementada.
Pueden considerarse una coleccion de pares llave-valor.
Se usan llave, y los pares se indican separando con dos puntos :  '''

# Ejemplo:

dic1 = { "a" : 0, "b" : 1}
print(dic1, "\n")



# Ejemplo 2:

dic2 = {"Leonor" : 554132578, "Arturo" : 55134256, "Arianna": 55678934}
print(dic2["Leonor"], "\n")



# Ejemplo 3:

dic3 = {}
dic3["Leo"] = 1233
dic3["Arturo"] = 657772
dic3["Ari"] = 8628
dic3["Leo"] = 896
print(dic3, "\n" )



# Diccionario or comprension:

dic4 = { i: i*i for i in range(1,11)}
print(dic4, "\n")



# ciclo sobre un diccionario:
for i in dic4:
    print(i) # Solo se imprime la llave.

del dic4[2] # Para borrar.

print(dic4)

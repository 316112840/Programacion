import random as r



# r es para lectura de archivos

archivo1 = open("Ejemplo1.txt", "r")

for linea in archivo1:
    print(linea)
    #print(linea.rstrip())   Con esto se quitan lineas vacias y espacios al final de la linea.

archivo1.close()
'''Para este ejemplo, primero necesite crear el archivo llamado "Ejemplo1.txt". '''







# w es para esritura de archivos

archivo2 = open("Ejemplo2.txt", "w")
archivo2.write("Lo que sea\n")
archivo2.close
'''En este ejemplo no fue necesario crear el archivo, ya que al escribir "archivo2.write("Lo que sea")"
se creo el archivo y coloco "Lo que sea" en el. '''



archivo3 = open("Ejemplo3.txt", "w")
archivo3.write("ihiun\n")
archivo3.write("awardrcgg\n")
archivo3.write("jyyffxvbnm\n")
archivo3.close()




# Tambien podemos usar ciclos:
archivo4 = open("Ejemplo4.txt", "w")

for i in range(5):
    archivo4.write("Esta es una linea del archivo 4")

archivo4.close()



# Para concatenar:
archivo5 = open("Ejemplo5.txt", "w")

for i in range(1,6):
    archivo5.write("Esta es la linea " + str(i) + " del archivo 5 \n")

archivo5.close()






# Ejercicio:

ejercicio1 = open("Ejercicio1.txt", "w")


for i in range(10):
    L = ""
    for j in range(i*10+1 , (i+1)*10+1):
        L += str(j) + " "
        
    ejercicio1.write(L + "\n")
    

ejercicio1.close()









# Esto se hizo el 2 de mayo.

# Comando with, nos permite no incluir la linea de cerrar el archivo porque lo cierra solo.

with open("Ejemplo7.txt", "w") as Ejemplo7:
    Ejemplo7.write("Linea 1 del archivo")




# El modo a, lectura y escritura

with open("Ejemplo8.txt", "w") as Ejemplo8:
    Ejemplo8.write("hbtrdrexc\n")


with open("Ejemplo8.txt", "a") as Ejemplo8:
    Ejemplo8.write("jhgswsd\n")
    Ejemplo8.write("nhvvrwaj\n")


with open("Ejemplo8.txt", "r") as Ejemplo8:
    for linea in Ejemplo8:
        print(linea)






with open("Ejemplo9.txt", "w") as Ejemplo9:
    for i in range(5):
        Ejemplo9.write(str(r.random()) + "\n")


with open("Ejemplo9.txt", "r") as Ejemplo9:
    for linea in Ejemplo9:
        numero = float(linea)
        print(numero,)
    






with open("Ejemplo9.txt", "r") as Ejemplo9:
    suma = 0.0
    numeroLineas = 0
    for linea in Ejemplo9:
        numero = float(linea)
        suma = suma + numero
        print(numero)
        numeroLineas += 1

print("Promedio: ", suma/numeroLineas)

print("La suma fue de: ", suma)




# Comando split

with open("Ejemplo10.txt", "w") as Ejemplo10:
    Ejemplo10.write("ARI 123456789 25 \n")
    Ejemplo10.write("ERNESTO 145678923 27 \n")
    Ejemplo10.write("Adan 9876549 29 \n")

with open("Ejemplo10.txt", "r") as Ejemplo10:
    for linea in Ejemplo10:
        datos = linea.split() # Split separa cuando encuentre lo que haya entre parentesis. Si no se coloca nada, se separara cuando haya espacios.
        for cadena in datos:
            print(cadena)
    

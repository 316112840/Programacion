
# r es para lectura de archivos

archivo1 = open("Ejemplo1.txt", "r")

for linea in archivo1:
    print(linea)
    # print(linea.rstrip())   Con esto se quitan lineas vacias y espacios al final de la linea.

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



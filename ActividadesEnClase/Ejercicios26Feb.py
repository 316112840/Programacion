Q = "             "

print("ESTO ES DEL PRIMER EJERCICIO:")
cadena = "icruv"
n = len(cadena) 
for i in range(n):
    cadena = cadena + cadena[n-1-i]
print(cadena)
print(Q)

#Para invertir una cadena:
def Invertir(Cadena):
    n = len(Cadena)
    CadenaInvertida = ""
    for i in range(n):
        CadenaInvertida = CadenaInvertida + Cadena[n-1-i]
    return CadenaInvertida

print(Invertir("uuvytcycu"))
print(Q)
print("ESTO ES DEL SEGUNDO EJERCICIO:")

#El segundo ejercicio es sobre ver si una lista dada es un palindromo, si sí regresar "True"
def Palindromo(cadena):
    CadenaInvertida = Invertir(cadena)
    if cadena == CadenaInvertida:
        return True
    else:
        return False

print(Palindromo("asdffdsa"))
print(Q)


#Variable bandera
def Palindromo1(cadena):
    bandera = True
    n = len(cadena)
    for i in range(n):
        if cadena[i] != cadena[n-1-i]:
            bandera = False
    return bandera
print(Palindromo1("asdfdsa"))
print(Palindromo1("asdffdsa"))
print(Palindromo1("jvfrdv"))
print(Q)

def Palindromo2(cadena):
    bandera = True
    n = len(cadena) 
    for i in range(n//2): #Para que el ciclo terminé a la mitad de la cadena, ya que si la mitad es igial a la otra mitas, pues ya no es necesario verificar que esa otra mitad es igual a la primer mitad.
        if cadena[i] != cadena[n-1-i]:
            bandera = False
    return bandera
print(Palindromo2("asdfdsa"))
print(Palindromo2("asdffdsa"))
print(Palindromo2("jvfrdv"))
print(Q)

def Palindromo3(cadena):
    bandera = True
    n = len(cadena)
    for i in range(n//2):
        if cadena[i] != cadena[n-1-i]:
            bandera = False
            break
    return bandera
print(Palindromo3("asdfdsa"))
print(Palindromo3("asdffdsa"))
print(Palindromo3("jvfrdv"))
print(Q)

def Palindromo4(cadena):
    n = len(cadena)
    for i in range(n//2):
        if cadena[i] != cadena[n-1-i]:
            return False
    return True
print(Palindromo4("asdfdsa"))
print(Palindromo4("asdffdsa"))
print(Palindromo4("jvfrdv"))
print(Q)

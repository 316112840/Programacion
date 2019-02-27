
cadena = "icruv"
n = len(cadena) 
for i in range(n):
    cadena = cadena + cadena[n-1-i]
print(cadena)

def Invertir(Cadena):
    n = len(Cadena)
    CadenaInvertida = ""
    for i in range(n):
        CadenaInvertida = CadenaInvertida + Cadena[n-1-i]
    return CadenaInvertida

print(Invertir("uuvytcycu"))

#El segundo ejercicio es sobre ver si una lista dada es un palindromo, si sí regresar"True"


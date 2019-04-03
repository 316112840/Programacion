# El metodo "primo" se hizo la clase del viernes.
# Esta funcion recibira un numero "n" y vera si es primo:
def primo(n):
    if n == 1:
        return False # Ya que 1 no es primo
    
    divisor = 2
    while divisor*divisor <= n:
        if n%divisor == 0:
            return False
        divisor = divisor + 1
    return True



# Estos dos metodos recibiran una lisa de numeros y regresara una lista con los numeros primos que contenga: 
def filtrarPrimos(l):
    l2 = []
    for n in l:
        if primo(n):
            l2.append(n)
    return l2



def FiltrarPrimos(l):
    l2 = []
    N = len(l)
    for n in range(N):
        if primo(l[n]):
            l2.append(l[n])
    return l2
        
    
print(filtrarPrimos([1,2,3,4,7,9,13]))
print(FiltrarPrimos([1,2,3,4,7,9,13]), "\n")






# Tablas de multiplicar:
tablas = []
for i in range(1,11):
    fila = []
    for j in range(1,11):
        fila.append(i*j)
    tablas.append(fila)

for i in tablas:
    print (i)
print("\n")







# Listas por comprension:
l = []
for i in range(1,11):
    l.append(i)
print(l )


l = [ i for i in range(1,11) ] # Esta es la lista por comprension. Hacer esto es lo mismo que escribir lo de arriba.
print(l, "\n")


vectorNulo = [ 0 for i in range(10) ]
print(vectorNulo, "\n" )


matrizCeros = []
for i in range(5):
    fila = [0 for i in range(5) ] # Aqui se uso la lista por comprension.
    matrizCeros.append(fila)
for i in matrizCeros:
    print(i )
print("\n")


MatrizCeros = [ [ 0 for i in range(5) ] for i in range(5) ] # Esta es otra forma de escribir la matriz de arriba.
for i in MatrizCeros:
    print(i)
print("\n")



# Lista por comprension con condicional:
l = [ i for i in range(1,11) if i > 4 ]
print(l)

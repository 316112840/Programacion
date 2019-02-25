S = "=========================================================="

#Sucesión de Fibonacci:
ListaFib = [1,1]
for i in range(10):
    ListaFib.append( ListaFib[i] + ListaFib[i+1])
print(ListaFib)


print(S)

#Secuencia de Lucas:
ListaLucas = [2,1]
for i in range(10):
    ListaLucas.append( ListaLucas[i] + ListaLucas[i+1])
print(ListaLucas)


print(S)


#Tablas de multiplicar:
ListaTablas = []
for i in range(11):
    Fila = []
    for j in range(11):
        Fila.append(i*j)
    ListaTablas.append(Fila)
print(ListaTablas)


print(S)

for i in range(11):
    print(ListaTablas[i])


print(S)


for i in range(11):
    Fila = []
    for j in range(11):
        Fila.append(i*j)
    print(Fila)

print(S)


for i in range(1,10):
    if i%5==0:
        break
    print(i)

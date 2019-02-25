# Mariana Yasmin Martínez García
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio1.4: Ejercicio para punto extra sobre la tarea.


def CantidadNumFib(n):
    if n < 0 or type(n) == float:
        print("ERROR.",n, "no es un entero positivo. Favor de ingresar un entero positivo.")
    else:
        A = [1,1]
        for i in range (n + 1):
            A.append(A[i] + A[i+1])
        for j in range(len(A)):
            if n <= A[j]:
                break
        print("El índice del primer número de la suesión de Fibonacci que es mayor o igual a",n, "es:", j + 1)
        


S = "                    "
CantidadNumFib(9.1)
print(S)
CantidadNumFib(-3)
print(S)
CantidadNumFib(7)
print(S)
CantidadNumFib(21)
print(S)
CantidadNumFib(144)
print(S)
CantidadNumFib(378)


# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

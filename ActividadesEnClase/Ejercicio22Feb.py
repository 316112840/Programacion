#Este programa resibirá un número,y regresará el valor mínimo de la suma de números naturales que necesita para ser igual o mayor al número dado
def CantidadNum(n):
    if n < 0:
        return 0 
    A = 0
    for i in range( n + 1):
        A += i
        if A >= n:
            return i




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
        



print(CantidadNum(8))
CantidadNumFib(21)
        

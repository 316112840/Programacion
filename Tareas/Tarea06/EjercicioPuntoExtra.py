# -*- coding: utf-8 -*-
# Mariana Yasmin Martinez Garcia
# Correo: mariana_yasmin@ciencias.unam.mx
# Ejercicio 6.3: Ejercicio para punto extra sobre la tarea.


def primo(n):
    
    if n == 1:
        
        return False 
    
    divisor = 2
    while divisor*divisor <= n:
        
        if n%divisor == 0:
            
            return False
        
        divisor = divisor + 1
        
    return True






def ListaPrimos(l):
    
    l2 = []
    
    for n in l:
        
        if primo(n):
            l2.append(n)
            
    return l2





def ListaNaturales(N):

    Lista = [1]

    for i in range(N - 1):

        Lista.append( Lista[ len(Lista) - 1] + 1 )

    return Lista






def dicPrimos(N):

    L1 = ListaNaturales(N)
    L2 = ListaPrimos(L1)
    while N != len(L2):
        
        L1.append( L1[len(L1)-1] + 1)

    return L2
    





# PRUEBAS

a = dicPrimos(9)
print(a)




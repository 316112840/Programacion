

def moda(L):
    n = len(L)
    L.sort()
    maxRep = 0
    numRep = 0
    eleMasRep = l[0]
    i = 0
    
    while i < n:
        valorActual = L[i]
        numRep = 0

        while i < n and L[i] == valorActual:
            numRep += 1
            i += 1

        if numRep > maxRep:
            maxRep = numRep
            eleMasRep = valorActual

    return eleMasRep


l = [ 1 ,2 , 2 , 2, 3 , 3 , 3 , 4 , 4 , 1 , 2 , 1 , 2 , 6 , 7 , 8 , 1]
print(moda(l))

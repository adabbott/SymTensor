import numpy as np
from itertools import combinations_with_replacement as cwr

def one(i):
    return i

def two(i,j,n):
    delta0 = 1 
    delta1 = n 
    result = one(j-i) 

    for a in range(1, i+1):
        result += delta1
        for b in range(1,a):
            result -= delta0
    return result

def three(i,j,k,n):
    delta0 = 1 
    delta1 = n 
    delta2 = n * (n + 1) / 2
    result = two(j-i,k-i,n-i)
    for a in range(1,i+1):
        result += delta2
        for b in range(1,a):
            result -= delta1
            for c in range(1,b):
                result += delta0
    return result

def four(i,j,k,l,n):
    delta0 = 1 
    delta1 = n 
    delta2 = n * (n + 1) / 2
    delta3 = n * (n + 1) * (n + 2) / 6
    result = three(j-i,k-i,l-i,n-i)
    for a in range(1,i+1):
        result += delta3
        for b in range(1,a):
            result -= delta2
            for c in range(1,b):
                result += delta1
                for d in range(1,c):
                    result -= delta0
    return result


def test(n, rank):
    # index funcs with rank to get function
    funcs = [one, one, two, three, four]
    f = funcs[rank]

    dim = np.arange(n)
    combos = np.asarray(list(cwr(dim, rank)))
    arr = np.zeros(rank * (n,), dtype=int)

    if rank == 2:
        for a,idx in enumerate(combos):
            i,j = idx
            arr[i,j] = a
        for idx in combos:
            i,j = idx
            print(f(i,j,n) == arr[i,j], end=' ')

    if rank == 3:
        for a,idx in enumerate(combos):
            i,j,k = idx
            arr[i,j,k] = a
        for idx in combos:
            i,j,k = idx
            print(f(i,j,k,n) == arr[i,j,k], end=' ')

    if rank == 4:
        for a,idx in enumerate(combos):
            i,j,k,l = idx
            arr[i,j,k,l] = a
        for idx in combos:
            i,j,k,l = idx
            print(f(i,j,k,l,n) == arr[i,j,k,l], end=' ')
    print(" ")
    print(" ")


test(6, 2)
test(6, 3)
test(6, 4)


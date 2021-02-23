import numpy as np
from itertools import combinations_with_replacement as cwr

def upper(n, rank, numer=1, denom=1):
    """
    Recursively determine the
    number of elements in upper triangle of
    symmetric tensor of rank `rank` with dimension size `n`
    FLOP counts: 5 * rank + 1, so linear scaling wrt rank. 6, 11, 16, 21, 26
    """
    if n < 1:
        return 0
    elif rank < 1:
        # this block has 1 flop
        return numer // denom
    else: # this block has 5 flops
        numer *= (n + (rank - 1))
        denom *= rank
        return upper(n, rank-1, numer, denom)

def one(i):
    return i

def two(i,j,n):
    result = one(j-i)
    result += upper(n, rank=1) * upper(i  , rank=1)
    result -= upper(n, rank=0) * upper(i-1, rank=2)
    return result

def three(i,j,k,n):
    result = two(j-i,k-i,n-i)
    result += upper(n, rank=2) * upper(i  , rank=1)
    result -= upper(n, rank=1) * upper(i-1, rank=2)
    result += upper(n, rank=0) * upper(i-2, rank=3)
    return result

def four(i,j,k,l,n):
    result = three(j-i,k-i,l-i,n-i)
    result += upper(n, rank=3) * upper(i  , rank=1)
    result -= upper(n, rank=2) * upper(i-1, rank=2)
    result += upper(n, rank=1) * upper(i-2, rank=3)
    result -= upper(n, rank=0) * upper(i-3, rank=4)
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
            f(i,j,n)
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

test(9, 2)
test(9, 3)
test(9, 4)

# Completely general approach using recursion
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
        
def flatten(n, rank, *args, result=0):
    """
    For a symmetric tensor of dimension size n and rank 'rank',
    recursively convert the multidimensional index *args = (i,j,k,...)
    to the corresponding 1d index in the flattened upper triangle
    of the symmetric tensor.
    """
    if rank == 0:
        return result
    elif rank == 1:
        return result + args[0]
    else:
        # Save i
        i = args[0]
        for alpha in range(1, rank + 1):
            result += (-1)**(alpha + 1) * upper(n, rank-alpha) * upper(i - alpha + 1, alpha)
        # Save new args, but cut off last one
        new_args = []
        for z in range(1, len(args)):
            new_args.append(args[z] - i)
        # Reduce n by i, reduce rank by 1, pass new i-reduced args and current result
        return flatten(n-i, rank-1, *new_args, result=result)

def test(n, rank):
    dim = np.arange(n)
    combos = np.asarray(list(cwr(dim, rank)))
    arr = np.zeros(rank * (n,), dtype=int)

    if rank == 2:
        for a,idx in enumerate(combos):
            i,j = idx
            arr[i,j] = a
        for idx in combos:
            i,j = idx
            print(flatten(n, rank, i,j))
            print(flatten(n, rank, i,j) == arr[i,j], end=' ')

    if rank == 3:
        for a,idx in enumerate(combos):
            i,j,k = idx
            arr[i,j,k] = a
        for idx in combos:
            i,j,k = idx
            print(flatten(n, rank, i,j,k) == arr[i,j,k], end=' ')

    if rank == 4:
        for a,idx in enumerate(combos):
            i,j,k,l = idx
            arr[i,j,k,l] = a
        for idx in combos:
            i,j,k,l = idx
            print(flatten(n, rank, i,j,k,l) == arr[i,j,k,l], end=' ')
    print(" ")
    print(" ")

test(9, 2)
test(9, 3)
test(9, 4)

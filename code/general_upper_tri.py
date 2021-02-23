import numpy as np
from itertools import combinations_with_replacement as cwr
from math import factorial
n = 6
dim = np.arange(n)

# Number of elements in the upper triangle of rank 'rank' tensor with dimension size n
def number_uppertri_elements(rank, n):
    return factorial(n + rank - 1) // (factorial(rank) * factorial(n - 1))

# Functions which map a tensor upper triangle index to flattened upper triangle index.
def one(i):
    return i

def two(i,j,n):
    delta =  n
    gamma = 1
    result = one(j-i)
    for a in range(1, i+1):
        result += delta
        for b in range(1, a):
            result -= gamma
    return result

def three(i,j,k,n):
    result = two(j-i, k-i, n-i)
    delta = n * (n+1) / 2
    gamma = n * 1
    for a in range(1, i+1):
        result += delta
        for b in range(1, a):
            result -= gamma - b + 1
    return result

# IN DEVELOPMENT
#def four(i,j,k,l,n):
#    print("i = ", i)
#    result = three(j-i, k-i, l-i, n-i)
#    delta = n * (n + 1) * (n + 2) / 6
#    gamma = n * (n + 1) / 2
#    tmp = 0
#    for a in range(1, i+1):
#        result += delta
#        tmp += delta
#        # Gotta get the leading index right... i=1 -> 6 i = 2--> 91 i = 3 --> 111 i =4 --> 121, i=5 125
#        for b in range(1, a):
#            #result -= gamma - n * (b + 1)
#            result -= gamma - (n * (b - 1))
#            #tmp -= gamma - 2 * (b + 1)
#            #tmp -= gamma - (n-b+1) #TODO try
#            # Doing -= gamma only makes i=2 case correct, and i=3 is 6 short
#            #tmp -= gamma 
#            # So for i = 3, if we do  - n * (b-1) it is now correct
#            #tmp -= gamma - (n * (b - 1))
#            # however i=4 is still wrong, off by 1
#            tmp -= gamma - (n * (b - 1))
#            #tmp -= gamma 
#            for c in range(1,b):
#                tmp -= c - 1 #n - b + 2
#                #tmp -= c #n - b + 2
#    print("i=",i,"leading idx",tmp)
#    return result
    
# This 4d case WORKS, but I do not know why. TODO derive equation compare to other dimension cases
def four(i,j,k,l,n):
    result = three(j-i, k-i, l-i, n-i)
    delta = n * (n + 1) * (n + 2) / 6
    gamma = n * (n + 1) / 2
    for a in range(1, i+1):
        result += delta
        for b in range(1, a):
            result -= gamma - (n * (b - 1))
            for c in range(1,b):
                result -= c - 1
    return result


# 2d case
rank = 2
combos = np.asarray(list(cwr(dim, rank)))
two_array = np.zeros(rank * (n,), dtype=int)
for a,idx in enumerate(combos):
    i,j = idx
    two_array[i,j] = a

print("2d case")
# Test 2d function
for idx in combos:
    i,j = idx
    print(two(i,j,n) == two_array[i,j], end =' ')
print("")

# 3d case
rank = 3
combos = np.asarray(list(cwr(dim, rank)))
three_array = np.zeros(rank * (n,), dtype=int)
for a,idx in enumerate(combos):
    i,j,k = idx
    three_array[i,j,k] = a

# Test 3d tensor function
print("3d case")
for idx in combos:
    i,j,k = idx
    print(three(i,j,k,n) == three_array[i,j,k], end=' ')
print("")

# 4d case
rank = 4
combos = np.asarray(list(cwr(dim, rank)))
four_array = np.zeros(rank * (n,), dtype=int)
for a,idx in enumerate(combos):
    i,j,k,l = idx
    four_array[i,j,k,l] = a

# Test 4d tensor function
print("4d case")
for idx in combos:
    i,j,k,l = idx
    print(four(i,j,k,l,n) == four_array[i,j,k,l], end=' ')
print("")


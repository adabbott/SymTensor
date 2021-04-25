# Symmetric Tensor Index Mappings
Suppose you have a symmetric tensor, but for the purpose of optimal memory management
you only want to store and work with the the unique elements. For example, the symmetric matrix 
```
A = [ 0  1  2  3 ]
    [ 1  4  5  6 ]
    [ 2  5  7  8 ]
    [ 3  6  8  9 ]
```
can be fully represented by a one-dimensional vector containing the elements of the upper triangle: 
```
A' = [ 0  1  2  3  4  5  6  7  8  9]
```

Mapping the index of elements in the full matrix to elements in the one-dimensional minimal representation
is trivial in this case. For a given 0-based index pair 
<p align="center">
<img src="images/eqn0.png" alt="eqn0" width="40"/>
<\p>
    
which indicate the address of an element in the matrix A,
the corresponding 1d index in the flattened upper triangle A' can be found by 

<img src="images/eqn1.png" alt="eqn1" width="300"/>
    
where n is the dimension size, in this case 4. It is  more tricky to derive is an analogous equation for the general case of an arbitrary rank symmetric tensor. That is, for a symmetric tensor of rank r, given a multidimensional index, we seek an expression to find the 1d index of the corresponding element in the flattened upper **hypertriangle**, which we call z. 
    
<img src="images/eqn2.png" alt="eqn2" width="200"/>

It is very likely such a relation has been derived before, but I could not find a reference after quite a lot of seaching around.

This repo serves as a reference implementation and a set of notes regarding the above problem. In the code folder is a recursive Python implementation of the index mapping. In the future, this repo may be extended to find the reverse mapping (1d index to multidimensional index, for a certain rank and dimension size) or perhaps explore implementations which take advantage of these concepts for the case of exploiting efficiencies in tensor contractions. 
    
# The Relation    
Without proof or derivation, this is the result, in its non-optimal but most descriptive form:
    
<img src="images/summary.pdf" alt="summary" width="500"/>


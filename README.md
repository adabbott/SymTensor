
This repo serves as a reference implementation and a set of notes regarding
the mathematics required for creating an index mapping between elements in
a general symmetric tensor and its flattened upper triangle. 
For example, a symmetric matrix has an equivalent upper and lower triangle,
and in the interest of performance one may wish to work with 
just the upper triangle as a flattened vector. 
The mapping of an index (i,j) to index z in the flattened vector representation 
is trivial, but the general case of a rank _r_ symmetric tensor mapping
an index to its flattened vector form is more complicated.

Here I derive analytic formulae which create a mapping multidimensional and unique single dimensional
indices, and include a recursion implementation in Python. 

By "upper triangle" of a totally symmetric tensor we mean all elements whose index [i,j,k,...] is such that i <= j <= k <= ...  
Some have referred to this section as the "upper hypertriangle" of a tensor.
These indices can be found easily in Python using itertools.
For a tensor with _r_ (rank) dimensions of size _n_: 

```python
from itertools import combinations_with_replacement as cwr
import numpy as np

rank = 2
size = 6
arr = np.arange(size)

combos = np.asarray(list(cwr(dim,rank)))
```

The result "combos" is every combination of indices such that i <= j, and i,j can run from 0 to 5. 
Indexing combos with some index idx with `combos[idx]` maps the _flattened generalized upper triangle_ index idx to the multidimensional index [i,j].

Given a pair `[i,j]`, you can also use binary search on `combos` to retrieve the flattened upper triangle index.
In this way, `combos` can serve as a mapping from the flattened upper triangle index to a unique multidimensional index, and vice versa. 
This is useful for mapping between frameworks which refer to the whole tensor and just one set of unique elements of the tensor.
The above script can be applied to any rank tensor of any dimension size by adjusting the `rank` and `size` variables.  
However, this requires one to store an array, effectively using it as a lookup table.

In the notes here I am interested in finding analytic formulae for mapping between the flattened upper triangle index 
and the unique multidimensional indices, and vice versa. This way, we do not need to generate the intermediate `combos` which essentially 
is serving as a lookup array. Computationally, this constitutes trading the memory overhead required to hold `combos` and the compute required to compute it
for instead functions which purely use operations involving `i`, `j`, and `size` to compute the flattened index. 

This is trivial in the 2-dimensional case, where you have a symmetric matrix and you want to map a pair of upper triangle indices [i,j] to the flattened 
upper triangle index. In fact, functions such as `numpy.triu_indices` can handle this for you.  I have not been able to find anywhere general formula
for arbitrary rank tensors, so here I derive them. 



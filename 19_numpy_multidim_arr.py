from numpy import *

arr = array([
    [1,2,3],
    [4,5,6]
])

print(arr)#o/p [[1 2 3][4 5 6]]
print(arr.dtype)#o/p int32
print(arr.ndim)#o/p 2 dimensions
print(arr.shape)#o/p (2,3) 2 rows, 3 colums
print(arr.size)#o/p total no of indexes
arr1 = arr.flatten()
print(arr1)#o/p multi to single

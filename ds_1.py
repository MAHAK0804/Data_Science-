
import numpy as np

np.__version__

# '2.0.0'

a = np.array([1,2,3])
a
# array([1, 2, 3])
a.shape
# (3,)
a.dtype
# dtype('int64')
a.ndim
# 1
a.size
# 3
a.itemsize
# 8


b=a*np.array([2,0,3])
b
# array([2, 0, 9])


l=[1,2,3]

a= np.array([1,2,3])

l.append(4)
l =l+ [5]
print(l)
# [1, 2, 3, 4, 5]

a = a+ np.array([5])
print(a)
# [6 7 8]


l1=[1,2,3]
l2=[4,5,6]
a1 = np.array(l1)
a2 = np.array(l2)
dot =0
dot = np.dot(a1,a2)
print(dot)
# 32

np.arange(0,5)
# array([0, 1, 2, 3, 4])

a=np.array([[1,2,3],[4,5,6]])
a.shape
# (2, 3)

a.reshape(3,2)
# array([[1, 2],
#        [3, 4],
#        [5, 6]])

a.ravel()
# array([1, 2, 3, 4, 5, 6])
a.min()
# np.int64(1)
a.max()
# np.int64(6)
a.sum()
# np.int64(21)

a.sum(axis=0)
# array([5, 7, 9])
a.sum(axis=1)
# array([ 6, 15])

np.sqrt(a)
# array([[1.        , 1.41421356, 1.73205081],
#        [2.        , 2.23606798, 2.44948974]])


np.std(a)
# np.float64(1.707825127659933)


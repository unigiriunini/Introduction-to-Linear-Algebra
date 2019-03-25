import numpy
import scipy.linalg as linalg

K = numpy.array([
        [2, -1, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0],
        [0, -1, 2, -1, 0, 0],
        [0, 0, -1, 2, -1, 0],
        [0, 0, 0, -1, 2, -1],
        [0, 0, 0, 0, -1, 2],
        ])

P, L, U = linalg.lu(K)
print('L: ')
print(L)
print('U: ')
print(U)
print('LU: ')
print(numpy.dot(L, U))

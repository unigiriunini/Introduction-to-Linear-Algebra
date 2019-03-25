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

Kinv = linalg.inv(K)
print('K inverse: ')
print(Kinv)
print('\n7 * K inverse:')
print(7 * Kinv)

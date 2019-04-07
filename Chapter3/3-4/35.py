import numpy
import matplotlib.pyplot as plt

K = numpy.array([
    [2, -1, 0, 0, 0, 0, 0, 0, 0],
    [-1, 2, -1, 0, 0, 0, 0, 0, 0],
    [0, -1, 2, -1, 0, 0, 0, 0, 0],
    [0, 0, -1, 2, -1, 0, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, 0, -1, 2, -1, 0, 0],
    [0, 0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, 0, 0, 0, -1, 2],
    ])
b = numpy.array([10 for _ in range(9)])

ans = numpy.linalg.solve(K, b)
print('answer: ')
print(ans)

plt.plot(ans)
plt.show()

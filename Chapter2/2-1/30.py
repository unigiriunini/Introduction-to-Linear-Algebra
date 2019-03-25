import numpy as np

A = np.array([
    [0.8, 0.3],
    [0.2, 0.7],
    ])
u = np.array([1.0, 0.0])

for _ in range(100):
    bu = u
    u = np.dot(A, u)
    print(u)
    if np.array_equal(bu, u): break

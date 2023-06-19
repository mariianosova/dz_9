import numpy as np

matrix = np.loadtxt('matrix.txt', delimiter=' ')

a = matrix[:, :-1]
b = matrix[:, -1]

x = np.linalg.solve(a, b)

np.savetxt('solution.txt', x, fmt='%.1f')
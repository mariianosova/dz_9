import numpy as np


matrix = np.loadtxt('matrix.txt', delimiter=' ')
a = matrix[:, :-1]
b = matrix[:, -1]

determinant = np.linalg.det(a)
if determinant != 0:
  inverse = np.linalg.inv(a)
  x = np.dot(inverse, b)
  np.savetxt('solution.txt', x, fmt='%.1f')
else:
	print('Система уравнений не имеет решения')
        
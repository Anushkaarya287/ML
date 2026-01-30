import numpy as np

X = np.array([
    [2104, 5, 1, 45],
    [1416, 3, 2, 40],
    [1534, 3, 2, 30],
    [852,  2, 1, 36]
], float)

y = np.array([460, 232, 315, 178], float)


Xb = np.column_stack([np.ones(len(X)), X])


beta = np.linalg.inv(Xb.T @ Xb) @ (Xb.T @ y)

print("Coefficients:", beta)
print("X =\n", X)
print("y =", y)
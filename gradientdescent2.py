import numpy as np
import matplotlib.pyplot as plt

# data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 4, 2, 5, 6], dtype=float)

lr = 0.1
epochs = 100

def batch_gradient_descent(X, y, lr, epochs):
    b0, b1 = 1, 1
    m = len(X)

    for epoch in range(epochs):
        y_pred = b0 + b1 * X

        db0 = (1/m) * np.sum(y_pred - y)
        db1 = (1/m) * np.sum((y_pred - y) * X)

        b0 -= lr * db0
        b1 -= lr * db1

    return b0, b1

def stochastic_gradient_descent(X, y, lr, epochs):
    b0, b1 = 0, 0
    m = len(X)

    for epoch in range(epochs):
        for i in range(m):
            xi = X[i]
            yi = y[i]

            y_pred = b0 + b1 * xi

            db0 = (y_pred - yi)
            db1 = (y_pred - yi) * xi

            b0 -= lr * db0
            b1 -= lr * db1

    return b0, b1

# get parameters
b0_bgd, b1_bgd = batch_gradient_descent(X, y, lr, epochs)
b0_sgd, b1_sgd = stochastic_gradient_descent(X, y, lr, epochs)

print("Batch Gradient Descent:")
print("b0 =", b0_bgd, "b1 =", b1_bgd)

print("\nStochastic Gradient Descent:")
print("b0 =", b0_sgd, "b1 =", b1_sgd)


y_pred_bgd = b0_bgd + b1_bgd * X
y_pred_sgd = b0_sgd + b1_sgd * X

# plot
plt.figure(figsize=(8, 6))
plt.scatter(X, y, label="Actual Data", marker="o")
plt.plot(X, y_pred_bgd, label="Batch Gradient Descent")
plt.plot(X, y_pred_sgd, label="Stochastic Gradient Descent")

plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression using Gradient Descent")
plt.legend()
plt.grid(True)

plt.show()

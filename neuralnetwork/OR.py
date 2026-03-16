import numpy as np

X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],[1],[1],[1]])

weights = np.random.rand(2,1)
bias = np.random.rand(1)

learning_rate = 0.1

def sigmoid(x):
    return 1/(1+np.exp(-x))

for epoch in range(10000):
    z = np.dot(X,weights) + bias
    output = sigmoid(z)

    error = y - output
    weights += learning_rate * np.dot(X.T,error)
    bias += learning_rate * np.sum(error)

print(np.round(output))
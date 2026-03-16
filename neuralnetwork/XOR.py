import numpy as np

X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],[1],[1],[0]])

np.random.seed(1)

input_neurons = 2
hidden_neurons = 2
output_neurons = 1

W1 = np.random.uniform(size=(input_neurons, hidden_neurons))
b1 = np.random.uniform(size=(1, hidden_neurons))

W2 = np.random.uniform(size=(hidden_neurons, output_neurons))
b2 = np.random.uniform(size=(1, output_neurons))

learning_rate = 0.1

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

for epoch in range(10000):

    hidden_layer = sigmoid(np.dot(X,W1) + b1)
    output = sigmoid(np.dot(hidden_layer,W2) + b2)

    error = y - output

    d_output = error * sigmoid_derivative(output)
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer)

    W2 += hidden_layer.T.dot(d_output) * learning_rate
    W1 += X.T.dot(d_hidden) * learning_rate

print(np.round(output))
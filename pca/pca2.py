import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [4,11],
    [8,4],
    [13,5],
    [7,14]
])

print("Original Data:\n", X)

mean = np.mean(X, axis=0)
print("\nMean:", mean)

X_centered = X - mean
print("\nMean Centered Data:\n", X_centered)

cov_matrix = np.cov(X_centered.T)
print("\nCovariance Matrix:\n", cov_matrix)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)

plt.figure()

plt.scatter(X[:,0], X[:,1], label="Data Points")
plt.scatter(mean[0], mean[1], label="Mean")

for i in range(len(eigenvalues)):
    
    vector = eigenvectors[:,i] * np.sqrt(eigenvalues[i]) * 3
    
    plt.plot(
        [mean[0], mean[0] + vector[0]],
        [mean[1], mean[1] + vector[1]],
        label=f"PC{i+1}"
    )

plt.xlabel("X1")
plt.ylabel("X2")
plt.title("PCA Visualization")
plt.legend()

plt.show()
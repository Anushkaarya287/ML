import numpy as np

A = np.array([[1,1],
              [7,7]])

print("Matrix A:\n",A)

AT = A.T
print("\nStep 1: A^T\n",AT)

ATA = AT @ A
print("\nStep 2: A^T A\n",ATA)

eigenvalues, eigenvectors = np.linalg.eig(ATA)

print("\nStep 3: Eigenvalues of A^T A\n",eigenvalues)
print("\nStep 4: Eigenvectors (V)\n",eigenvectors)

singular_values = np.sqrt(eigenvalues)
print("\nStep 5: Singular Values\n",singular_values)

Sigma = np.zeros((2,2))
Sigma[0,0] = singular_values[0]
Sigma[1,1] = singular_values[1]

print("\nSigma Matrix\n",Sigma)

V = eigenvectors
print("\nMatrix V\n",V)

U = np.zeros((2,2))

for i in range(2):
    if singular_values[i] != 0:
        U[:,i] = (A @ V[:,i]) / singular_values[i]

print("\nMatrix U\n",U)

VT = V.T
print("\nMatrix V^T\n",VT)

print("\nVerification A = U Σ V^T")
print(U @ Sigma @ VT)
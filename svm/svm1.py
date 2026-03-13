import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

X = np.array([[2, 2], [4, 5], [7, 4]])
y = np.array([-1, 1, 1])

svm = SVC(kernel='linear', C=1000)
svm.fit(X, y)

w = svm.coef_[0]
b = svm.intercept_[0]

print("SVM MAXIMUM MARGIN HYPERPLANE")
print("="*50)
print(f"Data points:")
for i, (x1, x2) in enumerate(X):
    print(f"  ({x1}, {x2}) -> Class {y[i]}")

print(f"\nHyperplane equation: {w[0]:.2f}*x1 + {w[1]:.2f}*x2 + ({b:.2f}) = 0")
print(f"Simplified: {w[0]:.2f}x1 + {w[1]:.2f}x2 = {-b:.2f}")

support_vectors = svm.support_vectors_
print(f"\nSupport vectors: {support_vectors}")

margin = 1 / np.sqrt(np.sum(w**2))
print(f"Margin width: {margin:.4f}")

x_min, x_max = 0, 9
y_min, y_max = 0, 7

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 8))

plt.contour(xx, yy, Z, levels=[-1, 0, 1], colors=['red', 'black', 'blue'], linestyles=['--', '-', '--'])
plt.contourf(xx, yy, Z, levels=[-100, 0, 100], colors=['lightcoral', 'lightblue'], alpha=0.3)

for i, (x1, x2) in enumerate(X):
    if y[i] == -1:
        plt.scatter(x1, x2, c='red', s=200, marker='o', edgecolors='black', linewidth=2, label='Class -1' if i==0 else "")
    else:
        plt.scatter(x1, x2, c='blue', s=200, marker='s', edgecolors='black', linewidth=2, label='Class +1' if i==1 else "")
    plt.annotate(f'({x1},{x2})', (x1, x2), xytext=(5, 5), textcoords='offset points', fontsize=10)

for sv in support_vectors:
    plt.scatter(sv[0], sv[1], s=300, facecolors='none', edgecolors='green', linewidth=3, label='Support Vector' if np.array_equal(sv, support_vectors[0]) else "")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('X1', fontsize=12)
plt.ylabel('X2', fontsize=12)
plt.title('SVM Maximum Margin Hyperplane', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

print("\n" + "="*50)
print("PREDICTIONS:")
for x in X:
    pred = svm.predict([x])[0]
    print(f"Point ({x[0]}, {x[1]}) -> Predicted: {pred}")
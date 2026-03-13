import numpy as np
import matplotlib.pyplot as plt

data = np.array([[2, 6], [3, 4], [3, 8], [4, 7], [6, 2], [6, 4], [7, 3], [7, 4], [8, 5], [7, 6]])
point_names = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']

M1 = data[0]
M2 = data[4]

distances_m1 = np.linalg.norm(data - M1, axis=1)
distances_m2 = np.linalg.norm(data - M2, axis=1)

clusters = ['C1' if d1 <= d2 else 'C2' for d1, d2 in zip(distances_m1, distances_m2)]

c1_indices = [i for i, c in enumerate(clusters) if c == 'C1']
c2_indices = [i for i, c in enumerate(clusters) if c == 'C2']
c1_points = data[c1_indices]
c2_points = data[c2_indices]
c1_names = [point_names[i] for i in c1_indices]
c2_names = [point_names[i] for i in c2_indices]

plt.figure(figsize=(10, 8))

plt.scatter(c1_points[:, 0], c1_points[:, 1], c='red', s=200, label='Cluster C1', edgecolors='black', linewidth=1, zorder=3)
plt.scatter(c2_points[:, 0], c2_points[:, 1], c='blue', s=200, label='Cluster C2', edgecolors='black', linewidth=1, zorder=3)

plt.scatter([M1[0]], [M1[1]], c='red', marker='X', s=400, edgecolors='black', linewidth=2, label='Medoid M1 (X1)', zorder=4)
plt.scatter([M2[0]], [M2[1]], c='blue', marker='X', s=400, edgecolors='black', linewidth=2, label='Medoid M2 (X5)', zorder=4)

for i, name in enumerate(point_names):
    if name in c1_names:
        color = 'red'
        offset = (-8, 5)
    else:
        color = 'blue'
        offset = (5, -8)
    plt.annotate(name, (data[i, 0], data[i, 1]), xytext=offset, textcoords='offset points', 
                fontsize=10, fontweight='bold', color=color)

plt.xlabel('X Coordinate', fontsize=12)
plt.ylabel('Y Coordinate', fontsize=12)
plt.title('K-Medoids Clustering Results', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.legend(loc='upper right')
plt.xlim(1, 9)
plt.ylim(1, 9)

plt.tight_layout()
plt.show()

print(f"Cluster C1 points: {c1_names}")
print(f"Cluster C2 points: {c2_names}")
print(f"\nMedoid M1 (C1): X1 at (2, 6)")
print(f"Medoid M2 (C2): X5 at (6, 2)")
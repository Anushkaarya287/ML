import numpy as np
import matplotlib.pyplot as plt

data_points = np.array([2, 4, 10, 12, 3, 20, 30, 11, 25])

M1 = 3
M2 = 18

distances_m1 = np.abs(data_points - M1)
distances_m2 = np.abs(data_points - M2)

clusters = ['C1' if d1 <= d2 else 'C2' for d1, d2 in zip(distances_m1, distances_m2)]

c1_points = data_points[[i for i, c in enumerate(clusters) if c == 'C1']]
c2_points = data_points[[i for i, c in enumerate(clusters) if c == 'C2']]

plt.figure(figsize=(10, 6))

y_positions = np.zeros_like(data_points)
colors = ['red' if c == 'C1' else 'blue' for c in clusters]

plt.scatter(c1_points, np.zeros_like(c1_points), c='red', s=200, label='Cluster C1', edgecolors='black', linewidth=1, zorder=3)
plt.scatter(c2_points, np.zeros_like(c2_points), c='blue', s=200, label='Cluster C2', edgecolors='black', linewidth=1, zorder=3)

plt.scatter([M1], [0], c='red', marker='X', s=300, edgecolors='black', linewidth=2, label='Centroid M1 (3)', zorder=4)
plt.scatter([M2], [0], c='blue', marker='X', s=300, edgecolors='black', linewidth=2, label='Centroid M2 (18)', zorder=4)

for point in data_points:
    plt.axvline(x=point, ymin=0.45, ymax=0.55, color='gray', linestyle='--', alpha=0.3)

plt.yticks([])
plt.xlabel('Data Points', fontsize=12)
plt.title('K-Means Clustering Results', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)

for point in data_points:
    cluster = 'C1' if point in c1_points else 'C2'
    y_offset = -0.02 if cluster == 'C1' else 0.02
    plt.text(point, y_offset, f'{point}', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

print(f"Cluster C1 points: {sorted(c1_points)}")
print(f"Cluster C2 points: {sorted(c2_points)}")
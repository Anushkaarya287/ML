import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

data = np.array([[3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [6, 2], [7, 2], [8, 4], [3, 3], [2, 6], [3, 5], [2, 4]])
point_names = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12']

minPts = 4
eps = 1.9

dbscan = DBSCAN(eps=eps, min_samples=minPts)
clusters = dbscan.fit_predict(data)

print("DBSCAN Clustering Results")
print("="*40)
print(f"minPts = {minPts}, ε = {eps}")
print(f"Clusters: {len(set(clusters)) - (1 if -1 in clusters else 0)}")
print(f"Noise points: {list(clusters).count(-1)}")
print("\nPoint classifications:")

for i, name in enumerate(point_names):
    if clusters[i] == -1:
        print(f"{name}: NOISE")
    else:
        print(f"{name}: Cluster {clusters[i] + 1}")

plt.figure(figsize=(10, 8))

for i, name in enumerate(point_names):
    if clusters[i] == -1:
        plt.scatter(data[i, 0], data[i, 1], c='black', marker='x', s=150, linewidths=2)
        plt.annotate(name, (data[i, 0], data[i, 1]), xytext=(5, 5), textcoords='offset points', fontsize=10)
    else:
        colors = ['red', 'blue', 'green']
        plt.scatter(data[i, 0], data[i, 1], c=colors[clusters[i]], s=200, edgecolors='black', linewidth=1, alpha=0.7)
        plt.annotate(name, (data[i, 0], data[i, 1]), xytext=(5, 5), textcoords='offset points', fontsize=10)

plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'DBSCAN Clustering (minPts={minPts}, ε={eps})')
plt.grid(alpha=0.3)
plt.xlim(1, 9)
plt.ylim(1, 8)
plt.tight_layout()
plt.show()
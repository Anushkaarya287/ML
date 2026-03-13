import numpy as np
import matplotlib.pyplot as plt

similarity_matrix = np.array([
    [1.00, 0.10, 0.41, 0.55, 0.35],
    [0.10, 1.00, 0.64, 0.47, 0.98],
    [0.41, 0.64, 1.00, 0.44, 0.85],
    [0.55, 0.47, 0.44, 1.00, 0.76],
    [0.35, 0.98, 0.85, 0.76, 1.00]
])

point_names = ['P1', 'P2', 'P3', 'P4', 'P5']
threshold = 0.8
minPts = 2

print("DBSCAN Clustering Results")
print("="*40)
print(f"Similarity threshold = {threshold}, MinPts = {minPts}")

neighbors = {}
for i in range(len(point_names)):
    point_neighbors = []
    for j in range(len(point_names)):
        if i != j and similarity_matrix[i, j] >= threshold:
            point_neighbors.append(point_names[j])
    neighbors[point_names[i]] = point_neighbors

point_types = {}
for i, name in enumerate(point_names):
    if len(neighbors[name]) >= minPts:
        point_types[name] = "CORE"
    else:
        is_border = False
        for j, other in enumerate(point_names):
            if i != j and similarity_matrix[i, j] >= threshold and len(neighbors[other]) >= minPts:
                is_border = True
                break
        if is_border:
            point_types[name] = "BORDER"
        else:
            point_types[name] = "NOISE"

print("\nPoint classifications:")
for name in point_names:
    print(f"{name}: {point_types[name]}")

core = [name for name in point_names if point_types[name] == "CORE"]
border = [name for name in point_names if point_types[name] == "BORDER"]
noise = [name for name in point_names if point_types[name] == "NOISE"]

print(f"\nCore: {core}")
print(f"Border: {border}")
print(f"Noise: {noise}")

plt.figure(figsize=(8, 6))

for i, name in enumerate(point_names):
    if point_types[name] == "CORE":
        plt.scatter(i, 1, c='green', s=500, marker='o', edgecolors='black', linewidth=2)
    elif point_types[name] == "BORDER":
        plt.scatter(i, 1, c='orange', s=500, marker='s', edgecolors='black', linewidth=2)
    else:
        plt.scatter(i, 1, c='red', s=500, marker='x', linewidths=3)
    plt.annotate(name, (i, 1), xytext=(0, -30), textcoords='offset points', ha='center', fontsize=14, fontweight='bold')

for i in range(len(point_names)):
    for j in range(i+1, len(point_names)):
        if similarity_matrix[i, j] >= threshold:
            plt.plot([i, j], [1, 1], 'gray', linestyle='-', alpha=0.5, linewidth=2)

plt.xticks(range(len(point_names)), point_names)
plt.yticks([])
plt.title(f'DBSCAN Classification (Similarity ≥ {threshold})')
plt.xlim(-0.5, 4.5)
plt.ylim(0.5, 1.5)
plt.tight_layout()
plt.show()
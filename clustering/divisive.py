import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

distance_matrix = np.array([
    [0, 9, 3, 6, 11],
    [9, 0, 7, 5, 10],
    [3, 7, 0, 9, 2],
    [6, 5, 9, 0, 8],
    [11, 10, 2, 8, 0]
])

point_names = ['a', 'b', 'c', 'd', 'e']
dist_vector = squareform(distance_matrix)

print("HIERARCHICAL CLUSTERING")
print("="*50)

print("\nAGGLOMERATIVE CLUSTERING:")
print("-"*30)

Z_single = linkage(dist_vector, method='single')
Z_complete = linkage(dist_vector, method='complete')
Z_average = linkage(dist_vector, method='average')

print("Single Linkage steps:")
for i, merge in enumerate(Z_single):
    print(f"  Step {i+1}: Merge clusters at distance {merge[2]:.2f}")

print("\nComplete Linkage steps:")
for i, merge in enumerate(Z_complete):
    print(f"  Step {i+1}: Merge clusters at distance {merge[2]:.2f}")

print("\nAverage Linkage steps:")
for i, merge in enumerate(Z_average):
    print(f"  Step {i+1}: Merge clusters at distance {merge[2]:.2f}")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

dendrogram(Z_single, labels=point_names, ax=axes[0])
axes[0].set_title('Single Linkage')

dendrogram(Z_complete, labels=point_names, ax=axes[1])
axes[1].set_title('Complete Linkage')

dendrogram(Z_average, labels=point_names, ax=axes[2])
axes[2].set_title('Average Linkage')

plt.tight_layout()
plt.show()

print("\n" + "="*50)
print("DIVISIVE CLUSTERING:")
print("-"*30)

data_points = []
for i in range(len(point_names)):
    data_points.append({'name': point_names[i], 'index': i})

def divisive_clustering(points_indices, depth=0):
    if len(points_indices) <= 1:
        return [points_indices]
    
    max_dist = -1
    pair_to_split = None
    
    for i in range(len(points_indices)):
        for j in range(i+1, len(points_indices)):
            dist = distance_matrix[points_indices[i], points_indices[j]]
            if dist > max_dist:
                max_dist = dist
                pair_to_split = (points_indices[i], points_indices[j])
    
    if pair_to_split is None:
        return [points_indices]
    
    cluster1 = [pair_to_split[0]]
    cluster2 = [pair_to_split[1]]
    remaining = [idx for idx in points_indices if idx not in [pair_to_split[0], pair_to_split[1]]]
    
    for idx in remaining:
        dist_to_c1 = distance_matrix[idx, cluster1[0]]
        dist_to_c2 = distance_matrix[idx, cluster2[0]]
        
        if dist_to_c1 < dist_to_c2:
            cluster1.append(idx)
        else:
            cluster2.append(idx)
    
    result = []
    if cluster1:
        result.extend(divisive_clustering(cluster1, depth+1))
    if cluster2:
        result.extend(divisive_clustering(cluster2, depth+1))
    
    return result

initial_indices = list(range(len(point_names)))
final_clusters = divisive_clustering(initial_indices)

print("\nDivisive clustering process:")
print("Starting with all points in one cluster")
print("Repeatedly split the farthest apart points")

print("\nFinal clusters:")
for i, cluster in enumerate(final_clusters):
    cluster_names = [point_names[idx] for idx in cluster]
    print(f"Cluster {i+1}: {cluster_names}")

plt.figure(figsize=(8, 6))
for i, cluster in enumerate(final_clusters):
    x_pos = i
    for idx in cluster:
        plt.scatter(x_pos, idx, s=500, c=['red', 'blue', 'green', 'orange', 'purple'][i], 
                   edgecolors='black', linewidth=2)
        plt.annotate(point_names[idx], (x_pos, idx), xytext=(5, 5), 
                    textcoords='offset points', fontsize=12)

plt.xticks(range(len(final_clusters)), [f'Cluster {i+1}' for i in range(len(final_clusters))])
plt.yticks(range(len(point_names)), point_names)
plt.title('Divisive Clustering Result')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
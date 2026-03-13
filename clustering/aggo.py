import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
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

print("Hierarchical Clustering - Agglomerative")
print("="*60)

linkage_methods = ['single', 'complete', 'average', 'centroid']
method_names = {'single': 'Single Linkage', 'complete': 'Complete Linkage', 
                'average': 'Average Linkage', 'centroid': 'Centroid Linkage'}

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()

for idx, method in enumerate(linkage_methods):
    print(f"\n{method_names[method]}:")
    print("-"*40)
    
    Z = linkage(dist_vector, method=method)
    
    clusters = fcluster(Z, t=2, criterion='maxclust')
    
    print("Cluster assignments:")
    for i, name in enumerate(point_names):
        print(f"  {name}: Cluster {clusters[i]}")
    
    cluster1 = [point_names[i] for i in range(len(point_names)) if clusters[i] == 1]
    cluster2 = [point_names[i] for i in range(len(point_names)) if clusters[i] == 2]
    print(f"\n  Cluster 1: {cluster1}")
    print(f"  Cluster 2: {cluster2}")
    
    print(f"\n  Dendrogram height levels:")
    for i, merge in enumerate(Z):
        points_merged = int(merge[3])
        print(f"    Step {i+1}: Merge clusters with distance {merge[2]:.2f} ({points_merged} points)")
    
    dendrogram(Z, labels=point_names, ax=axes[idx], color_threshold=0)
    axes[idx].set_title(f'{method_names[method]}', fontsize=14, fontweight='bold')
    axes[idx].set_xlabel('Points')
    axes[idx].set_ylabel('Distance')
    axes[idx].grid(alpha=0.3)

plt.suptitle('Hierarchical Clustering - Different Linkage Methods', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("DETAILED CLUSTERING STEPS")
print("="*60)

for method in linkage_methods:
    print(f"\n{method_names[method]} Steps:")
    print("-"*40)
    Z = linkage(dist_vector, method=method)
    
    n_points = len(point_names)
    current_clusters = [[name] for name in point_names]
    
    for step, merge in enumerate(Z):
        i, j = int(merge[0]), int(merge[1])
        dist = merge[2]
        
        if i < n_points and j < n_points:
            merged = [point_names[i], point_names[j]]
            print(f"  Step {step+1}: Merge {point_names[i]} and {point_names[j]} (distance = {dist:.2f})")
        elif i < n_points and j >= n_points:
            cluster_j = current_clusters[j - n_points + 1]
            merged = [point_names[i]] + cluster_j
            print(f"  Step {step+1}: Merge {point_names[i]} with cluster {cluster_j} (distance = {dist:.2f})")
        elif i >= n_points and j < n_points:
            cluster_i = current_clusters[i - n_points + 1]
            merged = cluster_i + [point_names[j]]
            print(f"  Step {step+1}: Merge cluster {cluster_i} with {point_names[j]} (distance = {dist:.2f})")
        else:
            cluster_i = current_clusters[i - n_points + 1]
            cluster_j = current_clusters[j - n_points + 1]
            merged = cluster_i + cluster_j
            print(f"  Step {step+1}: Merge cluster {cluster_i} with cluster {cluster_j} (distance = {dist:.2f})")
        
        current_clusters.append(merged)
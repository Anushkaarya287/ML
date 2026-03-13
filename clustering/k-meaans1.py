import numpy as np
import matplotlib.pyplot as plt

points = np.array([
    [2,10],
    [2,5],
    [8,4],
    [5,8],
    [7,5],
    [6,4],
    [1,2],
    [4,9]
])

labels = ["A1","A2","A3","B1","B2","B3","C1","C2"]

k = 3

centroids = np.array([
    points[0],
    points[3],
    points[6]
])

for iteration in range(5):

    distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)

    clusters = np.argmin(distances, axis=1)

    new_centroids = np.array([
        points[clusters == i].mean(axis=0) for i in range(k)
    ])

    if np.all(centroids == new_centroids):
        break

    centroids = new_centroids

print("Final Centroids:\n", centroids)
print("Cluster Assignment:\n", clusters)

plt.figure()

colors = ['red','blue','green']

for i in range(k):
    cluster_points = points[clusters == i]
    plt.scatter(cluster_points[:,0], cluster_points[:,1], label=f"Cluster {i+1}")

plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=200, label="Centroids")

for i, txt in enumerate(labels):
    plt.text(points[i][0]+0.1, points[i][1]+0.1, txt)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("K-Means Clustering")
plt.legend()

plt.show()
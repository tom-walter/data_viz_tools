from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

original_centroids = np.array([[-2, -2], [2, 2]])

for n_samples in range(10, 1001, 20):
    plt.clf()
    X, _ = make_blobs(n_samples=n_samples, n_features=2, centers=original_centroids, cluster_std=1.5, random_state=0)
    found_centroids = KMeans(n_clusters=2, random_state=0).fit(X).cluster_centers_

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.title('KMeans Clustering')
    plt.scatter(X[:, 0], X[:, 1], marker='.', s=10, label='n_samples={}'.format(n_samples))
    plt.scatter(original_centroids[:, 0], original_centroids[:, 1], marker='*', color='g', s=100, label='Original Centroids')
    plt.scatter(found_centroids[:, 0], found_centroids[:, 1], marker='X', color='y', s=80, label='Found Centroids')
    plt.grid(alpha=.5)
    plt.legend(loc='lower right')
    plt.savefig('cluster' + str(n_samples) + '.jpg', facecolor='white', format='jpg')
    plt.pause(0.01)

plt.show()
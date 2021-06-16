from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

original_centroids = np.array([[-2, -3], [2, 2], [-2, 2.5], [2.5, -2]])

for n_samples in range(10, 1001, 20):
    plt.clf()
    X, y = make_blobs(n_samples=n_samples, n_features=2, centers=original_centroids, cluster_std=1.5, random_state=0)
    kms = KMeans(n_clusters=4, random_state=0).fit(X)
    pred_centroids = kms.cluster_centers_
    y_pred = kms.labels_

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.title('KMeans Clustering')
    plt.scatter(X[:, 0], X[:, 1], marker='o', s=10, c=y, cmap='gist_rainbow', label='n_samples={}'.format(n_samples))
    plt.scatter(original_centroids[:, 0], original_centroids[:, 1], marker='x', color='k', s=100, label='Original Centroids')
    plt.scatter(pred_centroids[:, 0], pred_centroids[:, 1], marker='+', color='r', s=80, label='Predicted Centroids')
    plt.grid(alpha=.5)
    plt.legend(loc='lower right')
    plt.savefig('cluster' + str(n_samples) + '.jpg', facecolor='white', format='jpg')
    plt.pause(0.01)

plt.show()
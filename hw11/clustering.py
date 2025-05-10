from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def run_clustering():
    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

    kmeans = KMeans(n_clusters=3, random_state=42)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                c='red', s=200, alpha=0.5, marker='X')
    plt.title("K-Means Clustering Example")
    plt.show()

if __name__ == '__main__':
    run_clustering()

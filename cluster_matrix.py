from paths import *
import numpy as np
from sklearn.cluster import AgglomerativeClustering

distance_matrix = np.load(cluster_results_dir+"distance_matrix.npy")
print("Distance Matrix Loaded: ",distance_matrix.shape)


cluster = AgglomerativeClustering(n_clusters=8, affinity='precomputed', linkage='average').fit(distance_matrix)
labels = cluster.labels_
print(np.unique(labels,return_counts=True))

np.save(cluster_results_dir+"labels",labels)
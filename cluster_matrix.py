from paths import *
import numpy as np
import sklearn.cluster import DBSCAN

distance_matrix = np.save(cluster_results_dir+"distance_matrix.npy")
print("Distance Matrix Loaded: ",distance_matrix)

cluster = DBSCAN(min_samples = 100).fit(distance_matrix)
labels = cluster.labels_
print(labels.shape)

np.save(cluster_results_dir+"labels",labels)
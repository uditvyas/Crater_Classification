from paths import *
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score as sh_score

distance_matrix = np.load(cluster_results_dir+"distance_matrix.npy")
distance_matrix = distance_matrix*4/num_profiles
print("Distance Matrix Loaded: ",distance_matrix.shape)
all_2D_params = np.load(params_2D_save_dir+'all_2D_params.npy')


cluster = AgglomerativeClustering(n_clusters = None, distance_threshold=0.61, affinity='precomputed', linkage='complete').fit(distance_matrix)
print("Maximum of Distance Matrix is {}".format(np.max(distance_matrix)))
print("Minimum of Distance Matrix is {}".format(np.min(distance_matrix)))
print("Average of Distance Matrix is {}".format(np.mean(distance_matrix)))
print("Median of Distance Matrix is {}".format(np.median(distance_matrix)))
labels = cluster.labels_
print(np.unique(labels,return_counts=True))
np.save(cluster_results_dir+"labels",labels)
print("Silhouette Score: {}".format(sh_score(distance_matrix, labels, metric = "precomputed")))

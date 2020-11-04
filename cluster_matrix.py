from paths import *
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score as sh_score

distance_matrix = np.load(cluster_results_dir+"distance_matrix.npy")
print("Distance Matrix Loaded: ",distance_matrix.shape)
all_2D_params = np.load(params_2D_save_dir+'all_2D_params.npy')


cluster = AgglomerativeClustering(n_clusters = None, distance_threshold=0.8, affinity='precomputed', linkage='average').fit(distance_matrix)
labels = cluster.labels_
print(np.unique(labels,return_counts=True))
np.save(cluster_results_dir+"labels",labels)
print("Silhouette Score: ".format(sh_score(all_2D_params,labels)))

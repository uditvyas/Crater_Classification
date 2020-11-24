from paths import *
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score as sh_score

feature_vector = np.load(features_save_dir+"all_features.npy")

print("Features Loaded: ",feature_vector.shape)

cluster = AgglomerativeClustering(n_clusters = None, distance_threshold=0.90, linkage='complete').fit(feature_vector)
print("Maximum of Distance Matrix is {}".format(np.max(feature_vector)))
print("Minimum of Distance Matrix is {}".format(np.min(feature_vector)))
print("Average of Distance Matrix is {}".format(np.mean(feature_vector)))
print("Median of Distance Matrix is {}".format(np.median(feature_vector)))
labels = cluster.labels_
print(np.unique(labels,return_counts=True))
np.save(cluster_results_dir+"labels",labels)
print("Silhouette Score: {}".format(sh_score(feature_vector, labels, metric = "precomputed")))

import numpy as np
from paths import *
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

import matplotlib.pyplot as plt

all_features = np.load(features_save_dir+'all_features.npy')
labels = np.load(features_save_dir+'labels.npy')

distance_matrix = (all_features, metric = 'sqeuclidean')
distance_matrix = 1 - np.exp(distance_matrix)

dists = squareform(all_features)
linkage_matrix = linkage(dists, "single")
dendrogram(linkage_matrix, labels=labels)
plt.savefig(cluster_results_dir + "dendogram.jpg")
plt.show()
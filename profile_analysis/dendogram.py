import numpy as np
from paths import *
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

import matplotlib.pyplot as plt

distance_matrix = np.load(cluster_results_dir+"distance_matrix.npy")
labels = np.load(cluster_results_dir+"labels.npy")

dists = squareform(distance_matrix)
linkage_matrix = linkage(dists, "complete")
dendrogram(linkage_matrix, labels=labels)
plt.axvline(y = 0.91, c = 'red')
plt.savefig(cluster_results_dir + "dendogram.jpg")
plt.show()
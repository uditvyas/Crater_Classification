from paths import *
import numpy as np
import os
from shutil import copy
from tqdm import tqdm


names = np.load(names_dir+"names.npy")
labels = np.load(cluster_results_dir+"labels.npy")

n_clusters = np.unique(labels)

cluster_save_dir = cluster_results_dir + "Agglomerative_average_sqeuclidean/"

for label in range(len(n_clusters)):
    os.mkdir(cluster_save_dir+"cluster_{}".format(label))

for i in tqdm(range(len(labels))):
    which = labels[i]
    image = "ortho_" + names[i].split("_")[1] + '.tif'
    source = ortho_dir + image
    destination = cluster_save_dir + 'cluster_{}/'.format(which) + image
    copy(source,destination)
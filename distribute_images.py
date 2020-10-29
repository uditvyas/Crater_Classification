from paths import *
import numpy as np
import os
from shutil import copy
from tqdm import tqdm

names = np.load(names_dir+"names.npy")
labels = np.load(cluster_results_dir+"labels.npy")

n_clusters = np.unique(labels)

for label in range(len(n_clusters)):
    os.mkdir(cluster_results_dir+"cluster_{}".format(label))

for i in tqdm(range(len(labels))):
    which = labels[i]
    image = names[i] + '.tif'
    source = image_dir + image
    destination = cluster_results_dir + 'cluster_{}/'.format(which) + image
    copy(source,destination)
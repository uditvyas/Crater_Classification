from tqdm import tqdm
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from paths import *

all_features = np.load(features_save_dir+'all_features.npy')

num_clusters = 5
params = all_features
km = KMeans(n_clusters=num_clusters)
km_result = km.fit(params)
labels = km.labels_

tsne = TSNE(n_components=2, verbose=1)
tsne_results = tsne.fit_transform(params)
data = pd.DataFrame()
data['x'] = tsne_results[:,0]
data['y'] = tsne_results[:,1]
data['labels'] = labels
plt.figure(figsize=(15,15))
sns.scatterplot(x='x', y='y', 
                palette=sns.color_palette("hls",num_clusters),
                data = data,
                hue = 'labels',
                legend = 'full',
                alpha = 0.3)
plt.savefig(cluster_results_dir + "visual_cluster_5.jpg".format(j))
plt.close()

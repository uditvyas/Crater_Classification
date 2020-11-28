from tqdm import tqdm
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from paths import *

all_2D_profiles = np.load(resize_profiles_save_dir+'resampled_profiles.npy')
all_2D_profiles = np.mean(all_2D_profiles,axis=1)
labels = np.load(cluster_results_dir+'labels.npy')

profiles = all_2D_profiles

tsne = TSNE(n_components=2, verbose=1)
tsne_results = tsne.fit_transform(profiles)

data = pd.DataFrame()
data['x'] = tsne_results[:,0]
data['y'] = tsne_results[:,1]
data['labels'] = labels

plt.figure(figsize=(15,15))
sns.scatterplot(x='x', y='y', 
                palette=sns.color_palette("hls",len(np.unique(labels))),
                data = data,
                hue = 'labels',
                legend = 'full',
                alpha = 0.3)
plt.savefig(cluster_results_dir + "visual.jpg")
plt.close()


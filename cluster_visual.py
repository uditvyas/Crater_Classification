from tqdm import tqdm
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from paths import *

all_2D_params = np.load(params_2D_save_dir+'all_2D_params.npy')

for j in range(4):
    params = all_2D_params[:,j,:]
    km = KMeans(n_clusters=8)
    km_result = km.fit(params)
    labels = km.labels_
    
    tsne = TSNE(n_components=2, verbose=1)
    tsne_results = tsne.fit_transform(km_result)

    data = pd.DataFrame()
    data['x'] = tsne_results[:,0]
    data['y'] = tsne_results[:,1]
    data['labels'] = labels

    plt.figure(figsize=(15,15))
    sns.scatterplot(x='x', y='y', 
                    palette=sns.color_palette("hls",8),
                    data = data,
                    hue = 'labels',
                    legend = 'full',
                    alpha = 0.3)
    plt.savefig(cluster_results_dir + "visual_{}.jpg".format(j))
    plt.close()


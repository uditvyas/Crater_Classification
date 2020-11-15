from tqdm import tqdm
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from paths import *

all_features = np.load(features_save_dir+'all_features.npy')
print("Params Loaded: ",all_features.shape)

params = all_features
x = []
y = []
for i in tqdm(range(3,10)):
    
    # initialise and fit the Kmeams model
    kmeans = KMeans(n_clusters= i, random_state=0)
    result = kmeans.fit(params)
    print(result.labels_.shape)
    # append the number of clusters to x data list
    x.append(i)
    # append average within cluster sum of squares to y data set
    awcss = kmeans.inertia_/params.shape[0]
    y.append(awcss)
    print("Clusters = {}\tScore = {}".format(i,awcss))
plt.plot(x,y,'bo-')
plt.savefig(cluster_results_dir+"features_elbow.jpg")
plt.close()
from tqdm import tqdm
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from paths import *

all_2D_params = np.load(params_2D_save_dir+'all_2D_params.npy')
names = np.load(params_2D_save_dir+'names.npy')
print("Params Loaded: ",all_2D_params.shape)


for i in range(4):
    x = []
    y = []

    for i in tqdm(range(3,10)):
        params = all_2D_params[:,i,:]
        
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
    plt.savefig(cluster_results_dir+"profiles_i.jpg")
    plt.close()

# km = KMeans(n_clusters=4)
# result = km.fit(all_2D_params)
# labels = km.labels_
# print(labels)
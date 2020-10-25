from tqdm import tqdm
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from paths import *

all_2D_params = np.load(params_2D_save_dir+'all_2D_params.npy')
names = np.load(params_2D_save_dir+'names.npy')
print("Params Loaded: ",all_2D_params.shape)

x = []
y = []

for i in tqdm(range(1,3)):
    # initialise and fit the Kmeams model
    kmeans = KMeans(n_clusters= i, random_state=0)
    result = kmeans.fit(all_2D_params)

    print(result.labels_.shape)

    # append the number of clusters to x data list
    x.append(i)

    # append average within cluster sum of squares to y data set
    awcss = kmeans.inertia_/all_2D_params.shape[0]
    y.append(awcss)
    print("Clusters = {}\tScore = {}".format(i,awcss))

plt.plot(x,y,'bo-')
plt.show()

# km = KMeans(n_clusters=4)
# result = km.fit(all_2D_params)
# labels = km.labels_
# print(labels)
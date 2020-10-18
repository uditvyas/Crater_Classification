from utils import *
from paths import *

def curve_3D():
    pass

all_params = []
# for i in range(num_images):
#     mean = np.load(save_dir+'\mean_{}.npy'.format(i))
#     x = list(range(len(mean)))
#     x = [a-len(x)//2 for a in x]
#     param, var = curve_fit(curve_2D,x,mean)
#     all_params.append(param)
    
#     y,mse = cmp_fit(mean,param)
#     save_cmp(y, mean, mse, str(i), save_dir)

for i in range(num_images):
    name = image_dir + '\dem_' + str(i) + '.tif'
    I_dem = tifffile.imread(name)

    h,w = I_dem.shape
    # print(I_dem)

    x = np.array(list(range(w)))
    x = [a-len(x)//2 for a in x]
    X = []
    for item in x:
        xs = [item]*h
        for i in xs:
            X.append(i)
    
    y = np.array(list(range(h)))
    y = [a-len(y)//2 for a in y]
    Y = []
    for _ in range(w):
        for i in y:
            Y.append(i)

    I_dem = I_dem.flatten()
    X = np.array(X)
    Y = np.array(Y)
    print(X.shape)
    print(Y.shape)
    print(I_dem.shape)

    data = [X,Y]

    param,var = curve_fit(curve_3D,data,I_dem)


# all_params = np.array(all_params)
# x = []
# y = []

# for i in tqdm(range(3,10)):
#     # initialise and fit the Kmeams model
#     kmeans = KMeans(n_clusters= i, random_state=0)
#     result = kmeans.fit(all_params)

#     # append the number of clusters to x data list
#     x.append(i)

#     # append average within cluster sum of squares to y data set
#     awcss = kmeans.inertia_/all_params.shape[0]
#     y.append(awcss)
#     print("Clusters = {}\tScore = {}".format(i,awcss))

# plt.plot(x,y,'bo-')
# plt.show()

# km = KMeans(n_clusters=4)
# result = km.fit(all_params)
# labels = km.labels_
# print(labels)


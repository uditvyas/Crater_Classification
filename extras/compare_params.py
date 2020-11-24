from paths import *
import numpy as np
import matplotlib.pyplot as plt
from compare_params_utils import *
from tqdm import tqdm

# Distance Matrix
Matrix = np.zeros((num_images,num_images))

# Loading the names and Profiles
names = np.load(names_dir+'names.npy')
all_2D_params = np.load(params_2D_save_dir+'all_2D_params.npy')

for i in tqdm(range(len(names))):
    first_profiles = all_2D_params[i]
    for j in range(i+1,len(names)):
        second_profiles = all_2D_params[j]
        Matrix[i][j] = similarity(first_profiles,second_profiles,sigma)
        Matrix[j][i] = Matrix[i][j]
np.save(cluster_results_dir+"distance_matrix.npy", Matrix)
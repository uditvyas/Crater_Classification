from paths import *
import numpy as np
import matplotlib.pyplot as plt
from compare_profiles_utils import *
from tqdm import tqdm

# Distance Matrix
Matrix = np.zeros((num_images,num_images))

# Loading the names and Profiles
names = np.load(names_dir+'names.npy')
all_profiles = load_profiles(names,all_profiles_save_dir)
all_2D_params = np.load(params_2D_save_dir+'all_2D_params.npy')
resampled_profiles = np.load(resize_profiles_save_dir+'resampled_profiles.npy')
print("Resampled Profiles Loaded: ",resampled_profiles.shape)

for i in tqdm(range(len(names))):
    first_profiles = resampled_profiles[i]
    for j in range(i+1,len(names)):
        second_profiles = resampled_profiles[j]
        Matrix[i][j] = similarity(first_profiles,second_profiles,sigma)
        Matrix[j][i] = Matrix[i][j]
np.save(cluster_results_dir+"distance_matrix.npy", Matrix)
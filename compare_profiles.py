from paths import *
import numpy as np
import matplotlib.pyplot as plt
from compare_profiles_utils import *

# Distance Matrix
Matrix = np.zeros((num_images,num_images))

# Loading the names and Profiles
names = np.load(names_dir+'names.npy')
all_profiles = load_profiles(names,all_profiles_save_dir)

for i in range(len(names)):
    first_profiles = all_profiles[i]
    for j in range(i+1,len(names)):
        second_profiles = all_profiles[j]
        Matrix[i][j] = similarity(first_profiles,second_profiles)

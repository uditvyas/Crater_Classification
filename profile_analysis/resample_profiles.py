from paths import *
import numpy as np
import matplotlib.pyplot as plt
from compare_profiles_utils import *
from tqdm import tqdm
from scipy import signal

names = np.load(names_dir+'names.npy')
all_profiles = load_profiles(names,all_profiles_save_dir)
print("Profiles Loaded: ", len(all_profiles))
resampled_profiles = []

for profiles in tqdm(all_profiles):
    r_profiles = []
    for profile in profiles:
        profile = signal.resample(profile, resample_dimension)
        r_profiles.append(profile)
    r_profiles = np.array(r_profiles)
    resampled_profiles.append(r_profiles)

resampled_profiles = np.array(resampled_profiles)
np.save(resize_profiles_save_dir + "resampled_profiles", resampled_profiles)
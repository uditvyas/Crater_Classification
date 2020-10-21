import numpy as np
import paths
import tqdm.tqdm as tqdm
from analyse_curve_fit_utils import *

all_2D_params = np.load(params_2D_save_dir+'all_2D_params.npy')
print("Params Loaded: ",all_2D_params.shape)

all_profiles = []

names = os.listdir(all_profiles_save_dir)

for i in tqdm(range(num_images)):
    profiles = np.load(all_profiles_save_dir + names[i])
    params = all_2D_params[i]
    y_all = []
    mse_all = []
    for j in range(len(profiles)):
        y, mse = cmp_fit(profiles[i], params[i])
        y_all.append(y)
        mse_all.append(mse)
    save_cmp(y_all,profiles,mse_all,names[i],cmp_2D_save_dir)
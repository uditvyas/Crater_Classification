from paths import *
import numpy as np
import matplotlib.pyplot as plt
from compare_profiles_utils import *

names = np.load(names_dir+'names.npy')

all_profiles = []

for name in names:
    nm = name.split('.')[0]
    all_profiles.append(np.load(all_profiles_save_dir+'profiles_dem_{}.npy').format(nm))
print(len(all_profiles))
count = 0
for i in range(len(names)):
    first_name = names[i]
    # first_profile = np.load(all_profiles_save_dir+'profiles_{}.npy'.format(names[i]))
    
    first_profiles = all
    for j in range(i+1,len(names)):
        second_name = names[j]
        count +=1
print(count)

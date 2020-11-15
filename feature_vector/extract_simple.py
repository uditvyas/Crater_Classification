from paths import *
from extract_simple_utils import *
import numpy as np
import tifffile
from tqdm import tqdm

names = np.load(names_dir+"names.npy")
all_features = []
for i in tqdm(range(len(names))):
    name = image_dir + names[i]
    I_dem = tifffile.imread(name)
    depth = get_depth(I_dem)
    rim_height = get_rim_height(I_dem, depth)
    # rim_width = get_rim_width(I_dem,rim_height,depth)
    floor_diameter = get_floor_diameter(I_dem,depth)
    interior_volume = get_interior_volume(I_dem)
    features = []
    features.append(depth)
    features.append(rim_height)
    features.append(floor_diameter)
    features.append(interior_volume)
    features = np.array(features)
    all_features.append(features)
all_features = np.array(all_features)

maxes = np.max(all_features,axis=0)
all_features = all_features/maxes[:]

np.save(features_save_dir+'all_features.npy',all_features)
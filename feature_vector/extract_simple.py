from paths import *
from extract_simple_utils import *
import numpy as np
import tifffile
from tqdm import tqdm

names = np.load(names_dir+"names.npy")
for i in tqdm(range(len(names))):
    name = image_dir + names[i]
    I_dem = tifffile.imread(name)

    depth = get_depth(I_dem)
    print(depth)
    rim_height = get_rim_height(I_dem)
    rim_width = get_rim_width(I_dem)
    floor_diameter = get_floor_diameter(I_dem)
    interior_volume = get_interior_volume(I_dem)
    if(i==10):
        break
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
    rim_height = get_rim_height(I_dem, depth)
    # rim_width = get_rim_width(I_dem,rim_height,depth)
    floor_diameter = get_floor_diameter(I_dem,depth)
    print(i, floor_diameter)
    interior_volume = get_interior_volume(I_dem)
    
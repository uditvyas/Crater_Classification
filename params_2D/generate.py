from generate_utils import *
from paths import *
import numpy as np

profiles, names = generate_save_profiles(image_dir, all_profiles_save_dir, num_profiles)
np.save(names_dir+"names",np.array(names))
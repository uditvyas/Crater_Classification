from generate_utils import *
from paths import *

profiles, names = generate_save_profiles(image_dir, all_profiles_save_dir, num_images)
np.save(names_dir+"names",np.array(names))
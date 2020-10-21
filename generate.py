from generate_utils import *
from paths import *

profiles, means, names = generate_save_profiles(image_dir, profile_save_dir, num_images)

for i in tqdm(range(len(means))):
    save_mean_profile(mean = means[i], label = 'DEM: {}'.format(names[i]),
                        save_dir = figs_save_dir, name = names[i].split(".")[0])
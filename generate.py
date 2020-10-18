from utils import *

image_dir = '/media/HDD2/btech2/Crater/dataset_v1/dems/'
profile_save_dir = '/media/HDD2/btech2/Crater/Outputs/profiles/'
figs_save_dir = '/media/HDD2/btech/Crater/Outputs/profiles/figs/'
num_images = 2076

profiles, means, names = generate_profiles(image_dir, profile_save_dir, num_images)

for i in range(len(means)):
    save_mean_profile(mean = means[i], label = 'DEM: {}'.format(names[i]),
                        save_dir = figs_save_dir, name = names[i].split(".")[0])
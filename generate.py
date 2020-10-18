from utils import *

image_dir = '/media/HDD2/btech2/Crater/dataset_v1/dems/'
profile_save_dir = '/media/HDD2/btech2/Crater/Outputs/profiles/'
figs_save_dir = '/media/HDD2/btech/Crater/Outputs/profiles/figs/'
num_images = 2076

# ortho_name = [image_dir +  '\orthos\ortho_' + str(i_num) + '.tif']
profiles, means, names = generate_profiles(image_dir, profile_save_dir, num_images)

for i in range(len(means)):
    save_mean_profile(means[i],'DEM: {}'.format(names[i]), figs_save_dir, names[i])
from utils import *

image_dir = '/media/HDD2/btech2/Crater/dataset_v1/dems/'
save_dir = '/media/HDD2/btech2/Crater/Outputs/profiles/'
num_images = 2076

# ortho_name = [image_dir +  '\orthos\ortho_' + str(i_num) + '.tif']
profiles, means = generate_profiles(image_dir, save_dir, num_images)

# for i in range(len(means)):
    # plot_mean_profile(means[i],'DEM: {}'.format(i),save_dir,str(i))
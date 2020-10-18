import dependencies

image_dir = r'D:\Nitin Khanna Project\SAMPLE DATA\dems'
num_images = 10
save_dir = r'D:\\Nitin Khanna Project\\SAMPLE OUTPUT\\dems\\'

# ortho_name = [image_dir +  '\orthos\ortho_' + str(i_num) + '.tif']
profiles, means = generate_profiles(image_dir, save_dir, num_images)

for i in range(len(means)):
    plot_mean_profile(means[i],'DEM: {}'.format(i),save_dir,str(i))



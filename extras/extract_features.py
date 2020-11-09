from extract_features_utils import *
from paths import *
from tqdm import tqdm

##########################################################################################
## GENERATING 3D PARAMETERS
##########################################################################################

names = np.load(names_dir+"names.npy")
images,names = load_images(image_dir, names)
print("Images Loaded: {}".format(len(images)))
print("Names Loaded: {}".format(len(names)))

all_3D_params = []
print("Generating 3D parameters..")
for i in tqdm(range(num_images)):
    I_dem = images[i]
    xy_data = normalise_coordinates(I_dem)
    I_dem = I_dem.flatten()
    param,var = curve_fit(curve_3D,xy_data,I_dem)
    all_3D_params.append(param)
all_3D_params = np.array(all_3D_params)
np.save(params_3D_save_dir+"all_3D_params",all_3D_params)
print("3D Parameters Generated: ",all_3D_params.shape)


##########################################################################################
## GENERATING 2D PARAMETERS
##########################################################################################

all_2D_params = []
print(names[0])
for i in tqdm(range(num_images)):
    profiles = np.load(all_profiles_save_dir+'profiles_{}.npy'.format(names[i]))
    
    x = list(range(len(profiles[0])))
    x = [a-len(x)//2 for a in x]
    
    params = []
    for profile in profiles:
        minimum = np.min(profile)
        profile = profile - minimum
        param, var = curve_fit(curve_2D,x,profile)
        params.append(param)

    all_2D_params.append(params)
all_2D_params = np.array(all_2D_params)
np.save(params_2D_save_dir + "all_2D_params",all_2D_params)
##########################################################################################
##########################################################################################

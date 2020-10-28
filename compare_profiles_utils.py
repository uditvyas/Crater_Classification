import numpy as np

def load_profiles():
    all_profiles = []
    for name in names:
        nm = name.split('.')[0]
        all_profiles.append(np.load(all_profiles_save_dir+'profiles_{}.npy'.format(nm)))
    print("Profiles Loaded")


def similarity(first,second):
    return 0
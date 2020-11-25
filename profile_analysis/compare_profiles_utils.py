import numpy as np
from scipy.spatial.distance import euclidean, chebyshev, cosine
from paths import *

def load_profiles(names,directory):
    all_profiles = []
    for name in names:
        nm = name.split('.')[0]
        all_profiles.append(np.load(directory+'profiles_{}.npy'.format(nm)))
    print("Profiles Loaded")
    return all_profiles
'''
def compare(first,second,sigma):
    # cosine_distance = cosine(first,second)
    euclidean_distance = euclidean(first,second)
    # chebyshev_distance = chebyshev(first,second)
    which = euclidean_distance
    distance = 1 - np.exp(-which/(sigma**2))
    return distance
  
def similarity(first,second,sigma):
    n = first.shape[0]
    all_scores = []
    for i in range(n):
        local_sum = 0
        for j in range(n):
            local_sum += compare(first[j],second[(j+i)%n],sigma)
        all_scores.append(local_sum/num_profiles)
    distance = np.min(np.array(all_scores))
    return distance
'''
def compare(first,second,sigma):
    # cosine_distance = cosine(first,second)
    euclidean_distance = (first-second)**2
    euclidean_distance = np.sum(euclidean_distance)
    # chebyshev_distance = chebyshev(first,second)
    which = euclidean_distance
    distance = 1 - np.exp(-which/(sigma**2))
    return distance

def similarity(first,second,sigma):
    n = first.shape[0]
    all_scores = []
    print(first.shape,second.shape)
    for i in range(n):
        second_c = np.vstack((second[i:n,:],second[0:i,:]))
        local_sum = compare(first,second_c,sigma)
        all_scores.append(local_sum)
    distance = np.min(np.array(all_scores))
    return distance
import numpy as np
from scipy.spatial.distance import sqeuclidean, chebyshev, cosine, mahalanobis

def load_profiles(names,dir):
    all_profiles = []
    for name in names:
        nm = name.split('.')[0]
        all_profiles.append(np.load(dir+'profiles_{}.npy'.format(nm)))
    print("Profiles Loaded")
    
def compare(first,second,sigma):
    # cosine_distance = cosine(first,second)
    # sqeuclidean_distance = sqeuclidean(first,second)
    # chebyshev_distance = chebyshev(first,second)
    cov = np.cov(first, second)
    inv = np.linalg.inv(cov)
    mahalanobis_distance = mahalanobis(first, second, inv)
    distance = mahalanobis_distance
    # distance = 1 - np.exp(-which/(sigma**2))
    return distance
    
def similarity(first,second,sigma):
    n = first.shape[0]
    all_scores = []
    for i in range(n):
        local_sum = 0
        for j in range(n):
            local_sum += compare(first[j],second[(j+i)%n],sigma)
        all_scores.append(local_sum/4)
    distance = np.min(np.array(all_scores))
    return distance
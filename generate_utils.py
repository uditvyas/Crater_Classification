import matplotlib.pyplot as plt
import numpy as np
import cv2
import tifffile
import os
import csv
from PIL import Image
from scipy.optimize import curve_fit
from sklearn.cluster import KMeans
from tqdm import tqdm

'''
def get_profiles(img):
    if(img.shape[0]>img.shape[1]):
        img = img[:img.shape[0]-1,:]
    elif(img.shape[0]<img.shape[1]):
        img = img[:,:img.shape[1]-1]
    ctr = np.array(img.shape)//2
    profiles = []
    profiles.append(img[ctr[0],:])
    profiles.append(img[:,ctr[1]])
    profiles.append([img[a,a] for a in range(img.shape[0])])
    profiles.append([img[a,img.shape[0]-a-1] for a in range(img.shape[0])])
    
    labels = ['Profile Horizontal', 'Profile Vertical', 'Profile Right Down Diagonal', 'Profile Right Up Diagonal']
    return np.array(profiles),labels
'''
def plot_profiles(profiles,labels):
    n = profiles.shape[0]
    plt.figure(figsize=(10,10))
    rows = 2
    cols = 2
    x = range(profiles.shape[1])
    for i in range(rows * cols):
        plt.subplot(rows, cols, i + 1)
        plt.plot(x,profiles[i])
        plt.title(labels[i])
    plt.show()
'''
def get_mean_profile (profiles):
    mean_profile = np.mean([i for i in profiles],axis=0)
    return mean_profile

def save_mean_profile(mean, label, save_dir, name):
    x = range(mean.shape[0])
    x = [a-len(x)//2 for a in x]
    plt.plot(x,mean)
    plt.title(label)
    plt.savefig(save_dir + name + '.jpg')
    plt.clf()
'''

def get_profiles(img, profiles_per_image):
    n, m = img.shape
    n = min(n,m)
    delta_theta = 180//profiles_per_image
    thetas = []
    angle = 0
    while angle<180:
      thetas.append(angle)
      angle += delta_theta
    thetas = thetas[:-1]

    all_profiles = []
    for theta in thetas:
        profile = []
        if theta <=45 or theta>=135: 
            x = np.linspace(-n//2+1, n//2, num= n)
            y = np.floor(np.tan(theta*np.pi/180)*x)

        else:
            y = np.linspace(-n//2+1, n//2, num= n)
            x = np.floor(y/np.tan(theta*np.pi/180))
        if n%2:
            x = x + n//2
            y = y + n//2
        else:
            x = x + n//2 - 1
            y = y + n//2 - 1

        for i in range(n):
            profile.append(img[ int(y[i]) , int(x[i]) ])
        profile = np.array(profile)
        all_profiles.append(profile)
    all_profiles = np.array(all_profiles)
    labels = [str(i)+" degree" for i in thetas]

    return all_profiles, labels

def generate_save_profiles(dir, save_dir, num):
    print("Generating Profiles....")
    names = os.listdir(dir)
    all_profiles = []
    all_means = []
    for i in tqdm(range(len(names))):
        name = dir + names[i]
        I_dem = tifffile.imread(name)
        profiles,labels = get_profiles(I_dem)
        # plot_profiles(profiles,labels)
        # mean_profile = get_mean_profile(profiles)

        # small = np.min(mean_profile)
        # mean_profile = mean_profile - small

        # # plot_mean_profile(mean_profile,"mean")
        all_profiles.append(profiles)
        # all_means.append(mean_profile)

        np.save(save_dir+'profiles_{}'.format(names[i].split('.')[0]),profiles)
        # np.save(mean_profiles_save_dir+'mean_{}'.format(names[i].split('.')[0]),mean_profile)

    return all_profiles, names
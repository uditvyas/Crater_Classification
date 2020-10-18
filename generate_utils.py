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


def generate_profiles(dir, save_dir, num):
    print("Generating Profiles....")
    names = os.listdir(dir)
    all_profiles = []
    all_means = []
    for i in tqdm(range(len(names))):
        name = dir + names[i]
        I_dem = tifffile.imread(name)
        profiles,labels = get_profiles(I_dem)
        # plot_profiles(profiles,labels)
        mean_profile = get_mean_profile(profiles)

        small = np.min(mean_profile)
        mean_profile = mean_profile - small

        # # plot_mean_profile(mean_profile,"mean")
        all_profiles.append(profiles)
        all_means.append(mean_profile)

        np.save(save_dir+'all/profiles_{}'.format(i),profiles)
        np.save(save_dir+'means/mean_{}'.format(i),mean_profile)

    return all_profiles,all_means, names
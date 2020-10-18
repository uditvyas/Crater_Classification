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

def plot_mean_profile(mean,label, save_dir,name):
    x = range(mean.shape[0])
    plt.plot(x,mean)
    plt.title(label)
    plt.savefig(save_dir+'means\\'+name+'.jpg')
    plt.clf()


def generate_profiles(dir, save_dir, num):
    print("Generating Profiles....")
    names = os.listdir(dir)
    all_profiles = []
    all_means = []
    for i in tqdm(range(len(names))):
        name = dir + names[i]
        I_dem = tifffile.imread(name)
        print(I_dem.shape)
        # profiles,labels = get_profiles(I_dem)
        # plot_profiles(profiles,labels)
        # mean_profile = get_mean_profile(profiles)

        # small = np.min(mean_profile)
        # mean_profile = mean_profile - small

        # # plot_mean_profile(mean_profile,"mean")
        # all_profiles.append(profiles)
        # all_means.append(mean_profile)

        # np.save(save_dir+'profiles/profiles_{}'.format(i),profiles)
        # np.save(save_dir+'means/mean_{}'.format(i),mean_profile)

    return all_profiles,all_means


def get_3D_profile(img):
    img = Image.fromarray(img, 'Grayscale')
    img = img.resize((50,50))


def curve_2D(x,a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    return a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5 + a6*x**6 + a7*x**7 + a8*x**8 + a9*x**9 + a10*x**10
    
def cmp_fit(profile, params):
    x = list(range(len(profile)))
    x = [a-len(x)//2 for a in x]
    y = []
    for i in x:
        y.append(curve_2D(i,params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[9],params[10]))
    y = np.array(y)
    mse = np.mean((profile-y)**2)
    return y,mse

def save_cmp(y, profile, mse, label, save_dir):
    x = list(range(len(profile)))
    x = [a-len(x)//2 for a in x]
    plt.plot(x,profile)
    plt.plot(x,y)
    plt.title(label + " MSE: " + str(mse))
    plt.savefig(save_dir+"\{}.jpg".format(label))
    plt.clf()

def curve_3D(data,a0,a1,a2,a3):
    x = data[0]
    y = data[1]
    return x*y*a0
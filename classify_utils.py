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
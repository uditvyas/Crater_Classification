import numpy as np
from paths import *


def get_depth(img):
    n, m = img.shape
    n = min(n,m)        # radius = 1/3 n
    shape = int(n/3* depth_param)   # 1.15 times radius circle
    ext = (n - 2*shape)//2
    cropped_image = img[ext:n-ext+1, ext:n-ext+1].astype(np.float32)
    y,x = np.ogrid[-shape: shape+1, -shape: shape+1]
    mask = x**2+y**2 > shape**2
    cropped_image = cropped_image[:mask.shape[0], :mask.shape[0]]
    cropped_image[mask] = np.nan
    depth = np.nanmax(cropped_image) - np.nanmin(cropped_image)
    return depth

def get_rim_height(img, depth):
    n, m = img.shape
    n = min(n,m)        # radius = 1/3 n
    img = img[:n,:n]

    shape = int(n/3* rim_height_param)        # 1.4 times radius circle
    ext = (n - 2*shape)//2

    y,x = np.ogrid[-n//2: n//2, -n//2: n//2]
    mask = x**2+y**2 > shape**2

    img = img[:mask.shape[0], :mask.shape[0]]
    masked_image = img[mask]
    outside_avg = np.nanmean(masked_image)
    rim_height = depth - (outside_avg - np.min(img))
    return rim_height

def get_rim_width(img):
    rim_width = 0
    return rim_width

def get_floor_diameter(img):
    floor_diameter = 0
    return floor_diameter

def get_interior_volume(img):
    interior_volume = 0
    return interior_volume

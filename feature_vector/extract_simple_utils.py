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
    return np.max(0.0,rim_height)

def get_rim_width(img,rim_height,depth):
    n, m = img.shape
    radius = n//3
    outside_avg = depth - rim_height
    if rim_height<rim_width_param*outside_avg:
        return 0
    img[img>(1+rim_width_param)*outside_avg] = True
    y,x = np.ogrid[-n//2: n//2, -m//2: m//2]
    mask = x**2+y**2 < radius**2
    img[mask] = False
    return rim_width

def get_floor_diameter(img,depth):
    n, m = img.shape
    n = min(n,m)        # radius = 1/3 n
    radius = int(n/3)
    ext = (n - 2*shape)//2
    cropped_image = img[ext:n-ext+1, ext:n-ext+1].astype(np.float32)
    y,x = np.ogrid[-radius: radius+1, -radius: radius+1]
    mask = x**2+y**2 > radius**2
    cropped_image = cropped_image[:mask.shape[0], :mask.shape[0]]
    cropped_image[mask] = np.nan
    min_point = np.nanmin(cropped_image)
    r = 1
    while r<radius:
        image = cropped_image
        y,x = np.ogrid[-r: r+1, -r: r+1]
        mask1 = x**2+y**2 < r**2
        mask2 = x**2+y**2 > (r+1)**2
        image[mask1] = np.nan
        image[mask2] = np.nan
        num_pixels = np.count_nonzero(~np.isnan(image))
        useful_part = image[image<min_point + floor_diameter_threshold*depth]
        num_useful = np.count_nonzero(~np.isnan(useful_part))
        if ((num_pixels-num_useful)/num_pixels)>floor_diameter_tolerance:
            break
        r+=1
    floor_diameter = 2*r
    return floor_diameter

def get_interior_volume(img):
    interior_volume = 0
    return interior_volume

import numpy as np



def get_depth(img):
    n, m = img.shape
    n = min(n,m)        # radius = 1/3 n
    shape = int(n/3*1.15)

    ext = (n - 2*shape)//2

    img_1 = img[ext:n-ext+1, ext:n-ext+1].astype(np.float32)

    final_details = np.empty((shape,shape))
    
    y,x = np.ogrid[-shape: shape+1, -shape: shape+1]
    mask = x**2+y**2 > shape**2

    img_1 = img_1[:mask.shape[0]]
    img_1[mask] = np.nan

    depth = np.nanmax(img_1) - np.nanmin(img_1)

    return depth

def get_rim_height(img):
    rim_height = 0
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
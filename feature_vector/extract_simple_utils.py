import numpy as np



def get_depth(img):
    n, m = img.shape
    n = min(n,m)        # radius = 1/3 n
    shape = int(n/3*1.15)
    print(shape)
    ext = (n - 2*shape)//2

    img_1 = img[ext:n-ext, ext:n-ext]
    print(img_1.shape)
    # img_1 = img_1[:2*shape]
    final_details = np.empty((shape,shape))
    
    y,x = np.ogrid[-shape: shape+1, -shape: shape+1]
    mask = x**2+y**2 > shape**2

    img_1[mask] = np.NaN
    print(img_1)

    depth = 0

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
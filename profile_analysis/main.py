# Step 1: 
# Generating all the Profiles from the DEM images
import generate

# Step 2: 
# Normalising all the profiles so that analysis can be easily performed
import resample_profiles

# Step 3:
# Comparing pairs of images to generate distance matrix
import compare_profiles

# Step 4:
# Clustering based on the distance matrix
import cluster_matrix

# Step 5:
# Distributing the ortho images in their respective clusters
import distribute_images
import os
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as  np
from matplotlib.colors import LogNorm  # Import LogNorm for logarithmic color scale
from tqdm import tqdm
import json




# Directory where your .feather files are located
directory = 'annotations'

# List to store all data
data_list = []
num_files = len(os.listdir(directory)) #=850
progress = 0
counter = 0

pbar = tqdm(total=num_files, desc= "Progress: ")
# Iterate over all files in the directory
for filename in os.listdir(directory):
    #if(counter == 50):break
    counter+=1

    # Check if the file is a .feather file
    if filename.endswith(".feather"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Read the .feather file
        df = pd.read_feather(file_path)
        
        # Convert each row of the DataFrame to a list and append it to data_list
        for index, row in df.iterrows():
            data_list.append(row.tolist())
    pbar.update(1)
pbar.close()
print("Data loading is complete")
print("Number of loaded objects", len(data_list))

x_values = []
y_values = []
argo2_coords = []


for obj in data_list: 
    x = obj[10]
    y = obj[11]
    x_values.append(x)
    y_values.append(y)
    coord = (x, y)
    argo2_coords.append(coord)

with open("/Users/jonathanfossaert/Desktop/Bachlor Thesis/Statistics/BT_Codes/All Datasets - Data/360_Distribution/Argoverse2_xy_coord.json", "w") as f:
    json.dump(argo2_coords, f)

# x_values = [coord[0] for coord in coords]
# y_values = [coord[1] for coord in coords]

# Define plot limits
x_range = (-80, 80)
y_range = (-80, 80)

# Create histogram plot
sns.set(style="white")
plt.figure(figsize=(10, 8))

# Create linear bins
x_bins = np.linspace(x_range[0], x_range[1], 80)
y_bins = np.linspace(y_range[0], y_range[1], 80)

# Create the 2D histogram plot
hist = plt.hist2d(y_values, x_values, bins=[x_bins, y_bins], cmap='viridis',norm=LogNorm(), cmin=1)

plt.colorbar(label='Counts')#plt.colorbar(label='Counts')#
plt.xlabel('X Coordinates')
plt.ylabel('Y Coordinates')
plt.title('Argoverse 2 BEV Object Distribution')
plt.xlim(x_range)
plt.ylim(y_range)
plt.gca().set_aspect('equal', adjustable='box')  # Ensure aspect ratio is equal
plt.show()



import os
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as  np
from matplotlib.colors import LogNorm  
from tqdm import tqdm
import json


path ="PATH"

names = ["Argoverse2","KITTI","Waymo","nuScenes","ONCE","ZOD"]

# List of sample coordinates (replace these with your actual coordinates)
coords_list = []

for name in names: 
    filepath = path+name+"_xy_coord.json"
    with open(filepath, "r") as f:
        xy_coords = json.load(f)
    coords_list.append(xy_coords)
    print(name+" Load Complete")


# Define plot limits
x_range = (-100, 100)
y_range = (-100, 100)

# Create a 2x3 grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Loop through the coordinates lists and create plots in the grid
for i, (coords, ax) in enumerate(zip(coords_list, axes.flatten())):
    x_values = [coord[0] for coord in coords]
    y_values = [coord[1] for coord in coords]

    x_bins = np.linspace(x_range[0], x_range[1], 100)
    y_bins = np.linspace(y_range[0], y_range[1], 100)

    sns.set(style="white")
    hist = ax.hist2d(x_values, y_values, bins=[x_bins, y_bins], cmap='viridis', norm=LogNorm(), cmin=1)

    ax.set_title(names[i]+" BEV Object Distribution")
    ax.set_xlabel('X Coordinates')
    ax.set_ylabel('Y Coordinates')
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    ax.set_aspect('equal', adjustable='box')
    plt.colorbar(hist[3], ax=ax, label='Log Counts')

# Adjust layout and show plots
plt.tight_layout()
plt.show()

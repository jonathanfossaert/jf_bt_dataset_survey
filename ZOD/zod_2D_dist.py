import json 
import math
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import os
from tqdm import tqdm

# Define the path to the directory
dir_path = '~/data/zod/single_frames'

# Initialize an empty list to store the data

data_2d = []

# First, count the total number of directories
total_dirs = 200001

# Initialize a progress bar
pbar = tqdm(total=total_dirs, desc='Processing directories')


limit = 10000
counter = 0 
progress = 0

# Walk through the directory
for root, dirs, files in os.walk(dir_path):
    #if counter >= limit: break
    counter += 1 
    for file in files:
        # Check if the file is the one we're interested in
        if file == 'object_detection.json':
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Open the file and load the JSON data
            with open(file_path, 'r') as f:
                json_data = json.load(f)
                # Append the data to our list
                for item in json_data:
                    data_2d.append(item["geometry"]["coordinates"])
                    
    pbar.update(1)


pbar.close()

obj_bbox_center = []
x_values = []
y_values = []


# Image resolution : 3848x2168
for obj in data_2d:
    x_sum = sum(point[0] for point in obj)
    y_sum = sum(point[1] for point in obj)
    
    center_x = x_sum / len(obj)
    center_y = y_sum / len(obj)
    center = (center_x,center_y)
    obj_bbox_center.append(center)
    x_values.append(center_x)
    y_values.append(center_y)




d = {'X': x_values, 'Y': y_values}
data = pd.DataFrame(data=d)


sns.set(style="whitegrid")
plot = sns.displot(data=data,x = "X", y="Y", cmap="rocket", cbar=True)

plt.xlim(0,3848)
plt.ylim(0,2148)
plt.show()


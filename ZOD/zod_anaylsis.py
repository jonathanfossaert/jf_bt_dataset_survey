import json 
import math
import pandas as pd 
import numpy as np 
import os
from tqdm import tqdm

# Define the path to the directory
dir_path = '~/data/zod/single_frames'
# Initialize an empty list to store the data
data_3d = []
data_2d = []
data_classes = []
# First, count the total number of directories
total_dirs = 200001
# Initialize a progress bar
pbar = tqdm(total=total_dirs, desc='Processing directories')
limit = 30
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
                    if "location_3d" in item["properties"]:
                        data_3d.append(item["properties"]["location_3d"]["coordinates"])
                    data_classes.append(item["properties"]["class"])
    pbar.update(1)
pbar.close()
# Distance calulations 
zod_obj_distances = []

for item in data_3d:
    cx = item[0]
    cy = item[1]
    dist = math.sqrt((cx**2)+(cy**2))
    if(dist<251):
        zod_obj_distances.append(dist)

zod_data = pd.DataFrame(zod_obj_distances)
distances = np.array(zod_obj_distances)
filtered_distances = []
for item in zod_obj_distances:
    if (item >= 0) & (item <= 250):
        filtered_distances.append(item)

# Safe the data: 
with open("ZOD_Obj_Distances_<250.json", "w") as f:
    json.dump(filtered_distances, f)

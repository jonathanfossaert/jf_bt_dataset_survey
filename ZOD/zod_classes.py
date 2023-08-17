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
object_per_frame = []

# First, count the total number of directories
total_dirs = 200001

# Initialize a progress bar
pbar = tqdm(total=total_dirs, desc='Processing directories')

limit = 30
counter = 0 
progress = 0
class_distribution = {
    "num_lane_instances": 0,
    "num_vehicles": 0,
    "num_vulnerable_vehicles": 0,
    "num_pedestrians": 0,
    "num_traffic_lights": 0,
    "num_traffic_signs":0
}
data = []

# Walk through the directory
for root, dirs, files in os.walk(dir_path):
    #if counter >= limit: break
    counter += 1 
    for file in files:
        # Check if the file is the one we're interested in
        if file == 'metadata.json':
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Open the file and load the JSON data
            with open(file_path, 'r') as f:
                json_data = json.load(f)
                data.append(json_data)
    pbar.update(1)
pbar.close()

for frames in data: 
    for item,value in frames.items(): 
        if item in class_distribution:
            class_distribution[item] += value

print(class_distribution)

# Safe the data: 
filename = "zod_class_dist.json"
filepath = "$PATH TO STORE$"+filename
with open(filepath, "w") as f:
    json.dump(class_distribution, f)
import json 
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
            objects = 0
            with open(file_path, 'r') as f:
                json_data = json.load(f)
                # Append the data to our list
                if "num_lane_instances" in json_data:
                    objects += int(json_data["num_lane_instances"])                
                if "num_vehicles" in json_data:
                    objects += int(json_data["num_vehicles"])
                if "num_vulnerable_vehicles" in json_data:
                    objects += int(json_data["num_vulnerable_vehicles"])
                if "num_pedestrians" in json_data:
                    objects += int(json_data["num_pedestrians"])
                if "num_traffic_lights" in json_data:
                    objects += int(json_data["num_traffic_lights"])
                if "num_traffic_signs" in json_data:
                    objects += int(json_data["num_traffic_signs"])
                object_per_frame.append(objects)
    pbar.update(1)
pbar.close()

with open("ZOD_Obj_per_frames.json", "w") as f:
    json.dump(object_per_frame, f)
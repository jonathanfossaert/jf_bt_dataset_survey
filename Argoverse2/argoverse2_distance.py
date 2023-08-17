import os
import pandas as pd
import math
import json

# Directory where your .feather files are located
directory = 'annotations'
# List to store all data
data_list = []
num_files = len(os.listdir(directory))
progress = 0
counter = 0
# Iterate over all files in the directory
for filename in os.listdir(directory):
    if(progress==10):
        perc = int((counter/num_files)*100)
        print("Data loading at:",perc,"%" )
        progress = 0
    progress+=1
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
print("Data loading is complete")
print("Number of loaded objects", len(data_list))
object_distances = []

for obj in data_list: 
    x = obj[10]
    y = obj[11]
    dist = math.sqrt((x**2)+(y**2))
    object_distances.append(dist)

with open("Argoverse2_Obj_Distances.json", "w") as f:
    json.dump(object_distances, f)


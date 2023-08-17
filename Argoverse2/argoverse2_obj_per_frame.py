import os
import pandas as pd
import math
import seaborn as sns 
import matplotlib.pyplot as plt 
import json
from tqdm import tqdm
from collections import Counter




# Directory where your .feather files are located
directory = 'annotations'



# List to store all data
data_list = []
num_files = len(os.listdir(directory))
progress = 0
counter = 0

#pbar = tqdm(total=num_files, desc='Processing directories')


# Iterate over all files in the directory
for filename in os.listdir(directory):
    #if counter > 100: break
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
    #pbar.update(1)

#pbar.close()


print("Data loading is complete")
print("Number of loaded objects", len(data_list))

obj_per_frame = []

# for obj in data_list:
#     i = 0 
#     frame_time = obj[0]
#     for frame in data_list:
#         if frame[0] == frame_time:
#             i+=1
#         if frame[0]>frame_time: break
#     obj_per_frame.append(i)


frame_times = [inner_list[0] for inner_list in data_list]

obj_per_frame = Counter(frame_times)

# Print the counts
for time, count in obj_per_frame.items():
    print(f"Time {time} ns occurs {count} times.")


print(len(obj_per_frame))

with open("Argoverse2_Obj_per_frame .json", "w") as f:
    json.dump(obj_per_frame, f)

#print(obj_per_frame)
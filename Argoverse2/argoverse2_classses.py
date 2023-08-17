import os
import pandas as pd
import math
import seaborn as sns 
import matplotlib.pyplot as plt 
import json
from tqdm import tqdm


# Directory where your .feather files are located
directory = 'annotations'

# List to store all data
data_list = []
num_files = len(os.listdir(directory))
progress = 0
counter = 0

# Iterate over all files in the directory
for filename in os.listdir(directory):
    #if(counter == 30): break 

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

class_distribution = {
    "REGULAR_VEHICLE": 0,
    "PEDESTRIAN": 0,
    "BOLLARD": 0,
    "CONSTRUCTION_CONE": 0,
    "CONSTRUCTION_BARREL": 0,
    "STOP_SIGN": 0,
    "BICYCLE": 0,
    "LARGE_VEHICLE": 0,
    "WHEELED_DEVICE": 0,
    "BUS": 0,
    "BOX_TRUCK": 0,
    "SIGN": 0,
    "TRUCK": 0,
    "MOTORCYCLE": 0,
    "BICYCLIST": 0,
    "VEHICULAR_TRAILER": 0,
    "TRUCK_CAB": 0,
    "MOTORCYCLIST": 0,
    "DOG": 0,
    "WHEELED_RIDER": 0,
    "STROLLER": 0,
    "ARTICULATED_BUS": 0,
    "MESSAGE_BOARD_TRAILER": 0,
    #"MOBILE_PEDESTRIAN_SIGN": 0,
    "WHEELCHAIR": 0,
    "RAILED_VEHICLE": 0,
    "OFFICIAL_SIGNALER": 0,
    "TRAFFIC_LIGHT_TRAILER": 0,
    "ANIMAL": 0,
    "SCHOOL_BUS": 0,
    "MOBILE_PEDESTRIAN_CROSSING_SIGN": 0
}

for obj in data_list:
    categorie = obj[2]
    class_distribution[categorie] +=1

print(class_distribution)
print(len(class_distribution))

# Safe the data: 
filename = "argoverse2_class_dist.json"
filepath = "/Users/jonathanfossaert/Desktop/Bachlor Thesis/Statistics/BT_Codes/All Datasets - Data/Objects_per_Class/"+filename
with open(filepath, "w") as f:
    json.dump(class_distribution, f)


# # Create a figure and a single subplot
# fig, ax = plt.subplots()

# # Create a bar plot
# sns.barplot(x=list(class_distribution.keys()), y=list(class_distribution.values()))

# # Set a logarithmic scale on the y-axis
# ax.set_yscale('log')

# # Rotate x-labels if they are long
# plt.xticks(rotation=90)

# # Add a grid to the y-axis
# ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

# # Adjust the bottom margin to create more space for the x-labels
# plt.subplots_adjust(bottom=0.3)

# # Show the plot
# plt.show()

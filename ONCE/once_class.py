import json 
import math
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import os




directory = "labled_data"
annos_list = []
x=0
for root, _, files in os.walk(directory):
    #if x > 15:break
    x+=1
    for file in files:
        
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if 'frames' in data:
                    frames = data["frames"]
                    for anno in frames: 
                        if 'annos' in anno:
                            annos_list.append(anno["annos"])
print("Data loading complete")



class_distribution = {
    "Car": 0,
    "Cyclist": 0,
    "Truck": 0,
    "Bus": 0,
    "Pedestrian": 0,
}

for frame in annos_list:
    for obj in frame["names"]:
        class_distribution[obj]+=1
print(class_distribution)

# Safe the data: 
filename = "ONCE_class_dist.json"
filepath = "/Users/jonathanfossaert/Desktop/Bachlor Thesis/Statistics/BT_Codes/All Datasets - Data/Objects_per_Class/"+filename
with open(filepath, "w") as f:
    json.dump(class_distribution, f)
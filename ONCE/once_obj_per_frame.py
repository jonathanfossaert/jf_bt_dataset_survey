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
    #if x >15:break
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

obj_per_frame = []
for obj in annos_list:
    num_obj = len(obj["names"])
    obj_per_frame.append(num_obj)
#print(len(obj_per_frame))

with open("ONCE_Obj_per_frame.json", "w") as f:
    json.dump(obj_per_frame, f)
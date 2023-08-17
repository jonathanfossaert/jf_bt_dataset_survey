import json 
import math
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from tqdm import tqdm


file_path_anno = "v1.0-trainval_meta/v1.0-trainval/sample_annotation.json"
with open(file_path_anno, 'r') as f:
 anno_data = json.load(f) 

print("Annotation load complete")



pbar1 = tqdm(total=len(anno_data), desc='Processing data first time')

frame_dict = {}

for obj in anno_data: 
    frame_id = obj["sample_token"]
    
    if frame_id not in frame_dict:
       frame_dict[frame_id] = 0
    pbar1.update(1)
pbar1.close()

pbar2 = tqdm(total=len(anno_data), desc='Processing data second time')


for obj in anno_data:
   frame_id = obj["sample_token"]
   frame_dict[frame_id] += 1
   pbar2.update(1)
pbar2.close()
num_obj_per_frame = []
for key,count in frame_dict.items():
    num_obj_per_frame.append(count)
   



with open("nuScenes_Obj_per_frame_2.json", "w") as f:
    json.dump(num_obj_per_frame, f)









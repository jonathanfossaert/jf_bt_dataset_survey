import json 
import math
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from tqdm import tqdm


file_path_anno = "v1.0-trainval_meta/v1.0-trainval/instance.json"
with open(file_path_anno, 'r') as f:
 instance_data = json.load(f) 

file_path_anno = "v1.0-trainval_meta/v1.0-trainval/category.json"
with open(file_path_anno, 'r') as f:
 category_data = json.load(f)

categories = {}
for cat in category_data:
  cat_token = cat["token"]
  if cat_token not in categories:
    categories[cat_token]= 0


print("Data load complete")

bar = tqdm(total=len(instance_data),desc="Processing Data:")
for obj in instance_data:
  category = obj["category_token"]
  categories[category] += obj["nbr_annotations"]
  bar.update(1)
bar.close()

class_distribution = {}

for cat in category_data:
  key = cat["name"]
  token = cat["token"]
  class_distribution[key] = categories[token]



# Safe the data: 
filename = "nuScenes_class_dist.json"
filepath = "$PATH TO STORE$"+filename
with open(filepath, "w") as f:
    json.dump(class_distribution, f)
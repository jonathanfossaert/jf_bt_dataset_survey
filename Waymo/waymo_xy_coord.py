import json
import os 
from tqdm import tqdm

all_files = os.listdir("label_all/")
limit = 10000
a = 0
counter=0
bar = tqdm(total=len(all_files),desc="Data loading progress:")#198069
labels = []

for file in all_files:
    #if(counter>=limit):break
    filename="label_all/"+file
    with open(filename,'r') as data_file:
        for line in data_file:
            data = line.split()
            labels.append(data)
    counter = counter + 1
    bar.update(1)
bar.close()
index = 0
clear_labels = labels.copy()
x = 0
for typ in labels:
    clear_labels[x].pop(0) #name
    clear_labels[x].pop(0) #truncation
    clear_labels[x].pop(0) #occlusion   
    clear_labels[x].pop(0) #alpha
    clear_labels[x].pop(0) #bbox
    clear_labels[x].pop(0) #bbox
    clear_labels[x].pop(0) #bbox   
    clear_labels[x].pop(0) #bbox
    clear_labels[x].pop(0) #dimensions
    clear_labels[x].pop(0) #dimensions
    clear_labels[x].pop(0) #dimensions
    #clear_labels[x].pop(4) #location
    #clear_labels[x].pop(4) #location
    #clear_labels[x].pop(4) #location
    clear_labels[x].pop(1) #y
    clear_labels[x].pop(2) #rotation_y
    clear_labels[x].pop(2) #cam_idx
    x+=1

x_values=[]
y_values=[]
coords = []

for item in clear_labels:
    x = float(item[0])
    y = float(item[1])
    x_values.append(x)
    y_values.append(y)
    coord = (x,y)
    coords.append(coord)

path = "$PATH TO STORE$"
name = "waymo_xy_coord.json"
    
with open(path+name, "w") as f:
    json.dump(coords, f)

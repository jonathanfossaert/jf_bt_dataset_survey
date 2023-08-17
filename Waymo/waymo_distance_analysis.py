import math
import os 
import json


all_files = os.listdir("label_all/")
limit = 300
a = 0
counter = 0
labels = []
for file in all_files:
    #if(counter==limit):break
    a = a+1
    filename="label_all/"+file
    
    with open(filename,'r') as data_file:
        for line in data_file:
            data = line.split()
            labels.append(data)
    if(a==1000):
        perc = counter / len(all_files)
        print("Progress of Data loading: ",perc)
        a = 0
    counter = counter + 1
print("Progress of Data loading:  1.0000000000000000")
print("Reading Data finished")

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

item_distances = []
for item in clear_labels:
    x = float(item[0])
    y = float(item[1])
    #z = float(item[2]) 
    dist = math.sqrt((x**2)+(y**2))
    #print(x,y,dist)
    item_distances.append(dist)

with open("Waymo_Obj_Distances.json", "w") as f:
    json.dump(item_distances, f)

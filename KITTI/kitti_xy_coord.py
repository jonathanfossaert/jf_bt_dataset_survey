import os
import json

labels = []
all_files = os.listdir("kitti_lables/")
limit = 1000
a = 0

for file in all_files :
    if(file[7]!="t"): continue
    #if(a==limit):break
    a = a+1
    filename="kitti_lables/"+file
    with open(filename,'r') as data_file:
        for line in data_file:
            data = line.split()
            labels.append(data)

copy_labels = labels.copy() 

for typ in labels:
    #print(typ[0])
    if(typ[0]=='DontCare'):
        copy_labels.remove(typ)
        
clear_labels = copy_labels.copy()
x = 0
for typ in copy_labels:
    clear_labels[x].pop(0) #name
    clear_labels[x].pop(0) #truncation
    clear_labels[x].pop(0) #occlusion   
    clear_labels[x].pop(0) #alpha
    clear_labels[x].pop(0) #2dbbox
    clear_labels[x].pop(0) #2dbbox
    clear_labels[x].pop(0) #2dbbox
    clear_labels[x].pop(0) #2dbbox
    clear_labels[x].pop(0) #dimensions
    clear_labels[x].pop(0) #dimensions
    clear_labels[x].pop(0) #dimensions
    clear_labels[x].pop(1) #y
    clear_labels[x].pop(2) #rotationy
    #cleared_car_labels[x].pop(3) #score
    x+=1

coords = []
x_coord=[]
y_coord=[]

for item in clear_labels:
    x = float(item[0])
    y = float(item[1])
    x_coord.append(x)
    y_coord.append(y)
    coord = (x,y)
    coords.append(coord)

path = "PATH to store"
name = "kitti_xy_coord.json"
    
with open(path+name, "w") as f:
    json.dump(coords, f)


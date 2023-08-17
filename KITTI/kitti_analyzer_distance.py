import math 
import os
import json




filename = '0'
#7480

labels = []
#198069

all_files = os.listdir("kitti_lables/")

limit = 1000
a = 0

for file in all_files :
    if(file[7]!="t"): continue
    #if(a==limit):break
    a = a+1
    #filename= '%07d' % (int(i) )
    filename="kitti_lables/"+file
    with open(filename,'r') as data_file:
        for line in data_file:
            
            data = line.split()
            labels.append(data)

index = 0
copy_labels = labels.copy() 
#print(copy_labels)

for typ in labels:
    #print(typ[0])
    if(typ[0]=='DontCare'):
        #print(typ[0])
        #print(labels[index])
        copy_labels.remove(typ)
        #print(index)
        
    index+=1

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

count_100 = 0
item_distances = []
for item in clear_labels:
    x = float(item[0])
    y = float(item[1])
    #z = float(item[2]) 
    dist = math.sqrt((x**2)+(y**2))
    item_distances.append(dist)
    if(dist>80): count_100 = count_100 + 1


with open("KITTI_Obj_Distances.json", "w") as f:
    json.dump(item_distances, f)




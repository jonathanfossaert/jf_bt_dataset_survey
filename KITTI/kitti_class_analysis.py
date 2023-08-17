import math
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import os 
import json 




filename = '0'
#7480

labels = []
#198069

all_files = os.listdir("kitti_lables/")

limit = 7479
a = 0

for file in all_files :
    if(file[7]!="t"): continue
    #if(a==limit):break
    #a = a+1
    #filename= '%07d' % (int(i) )
    filename="kitti_lables/"+file
    #print(file)
    with open(filename,'r') as data_file:
        for line in data_file:
            
            data = line.split()
            labels.append(data)
        


index = 0
clear_labels = labels.copy()
x = 0
for typ in labels:
    #clear_labels[x].pop(0) #name
    clear_labels[x].pop(1) #truncated
    clear_labels[x].pop(1) #occluded
    clear_labels[x].pop(1) #alpha
    clear_labels[x].pop(1) #bbox
    clear_labels[x].pop(1) #bbox
    clear_labels[x].pop(1) #bbox
    clear_labels[x].pop(1) #bbox
    clear_labels[x].pop(1) #dim
    clear_labels[x].pop(1) #dim
    clear_labels[x].pop(1) #dim
    clear_labels[x].pop(1) #location
    clear_labels[x].pop(1) #location
    clear_labels[x].pop(1) #location
    clear_labels[x].pop(1) #rotation_y
    #clear_labels[x].pop(1) #cam_idx
    x+=1

# for x in clear_labels: 
#       print(x)

# Classes:
#     Car
#     Cyclist
#     Van
#     Dont care
#     Misc
#     Pedestrian
#     Truck
#     Pedestrian(sitting)
#     Tram

num_peds=0
num_cars=0
num_cyclist=0
num_van=0
num_misc=0
num_truck=0
num_ped_sit=0
num_tram=0



for item in clear_labels:
   if(item[0]=='DontCare'): continue
   if(item[0]=='Car'): num_cars = num_cars + 1
   if(item[0]=='Pedestrian'): num_peds = num_peds + 1
   if(item[0]=='Cyclist'):num_cyclist =num_cyclist + 1
   if(item[0]=='Misc'): num_misc = num_misc + 1
   if(item[0]=='Truck'): num_truck = num_truck + 1
   if(item[0]=='Tram'): num_tram = num_tram + 1
   if(item[0]=='Pedestrian(sitting)'): num_ped_sit = num_ped_sit +1

kitti_class = {
    "Car": num_cars,
    "Pedestrian": num_peds,
    "Cyclist": num_cyclist,
    "Truck": num_truck,
    "Tram": num_tram,
    "misc":num_misc,
    "Pedestrian(sitting)": num_ped_sit
}


# Safe the data: 
filename = "KITTI_class_dist.json"
filepath = "$PATH TO STORE$"+filename
with open(filepath, "w") as f:
    json.dump(kitti_class, f)

print("Number of cars: ",num_cars)
print("Number of Pedestrians: ",num_peds)
print("Number of Pedestrians sitting : ",num_ped_sit)
print("Number of Truck: ",num_truck)
print("Number of Tram: ",num_tram)
print("Number of Cyclsit: ",num_cyclist)
print("Number of Misc: ",num_misc)
print("Number of Objects in total: ", len(clear_labels))

# data = pd.DataFrame(class_data)

# plot = sns.violinplot(data=data)
# plot.set(ylabel="Distance in meters ")
# plt.show()

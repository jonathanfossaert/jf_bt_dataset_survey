
import os 
import json
from tqdm import tqdm

labels = []
all_files = os.listdir("label_all/")
limit = 10000
a = 0
bar = tqdm(total =len(all_files), desc= "Data loading Progress ")

for file in all_files :
    #if(a==limit):break
    a = a+1
    #filename= '%07d' % (int(i) )
    filename="label_all/"+file
    
    with open(filename,'r') as data_file:
        for line in data_file:
            data = line.split()
            labels.append(data)
    bar.update(1)
bar.close()

index = 0
clear_labels = labels.copy()
x = 0
for typ in labels:
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
    clear_labels[x].pop(1) #cam_idx
    x+=1

num_peds=0
num_cars=0
num_cyclist=0
for item in clear_labels:
   if(item[0]=='Car'): num_cars = num_cars + 1
   if(item[0]=='Pedestrian'): num_peds = num_peds + 1
   if(item[0]=='Cyclist'):num_cyclist =num_cyclist + 1

print("Number of cars: ",num_cars)
print("Number of Pedestrians: ",num_peds)
print("Number of Cyclsit: ",num_cyclist)

waymo_class = {
    "Car": num_cars,
    "Pedestrian": num_peds,
    "Cyclist": num_cyclist,

}
# Safe the data: 
filename = "Waymo_class_dist.json"
filepath = "$PATH TO STORE$"+filename
with open(filepath, "w") as f:
    json.dump(waymo_class, f)


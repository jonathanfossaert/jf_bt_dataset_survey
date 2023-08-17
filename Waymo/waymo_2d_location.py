import math
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import os 



filename = '0'
#7480
all_files = os.listdir("label_all/")

limit = 1000
a = 0

counter = 0
labels = []
#198069
for file in all_files:
    #if(a==limit):break
    a = a+1
    #filename= '%07d' % (int(i) )
    filename="label_all/"+file
    
    with open(filename,'r') as data_file:
        for line in data_file:
            data = line.split()
            labels.append(data)
    if(a==5000):
        perc = counter / len(all_files)
        print("Progress of Data loading: ",perc)
        a = 0
    counter = counter + 1
    
index = 0
clear_labels = labels.copy()
x = 0
for typ in labels:
    clear_labels[x].pop(0) #name
    clear_labels[x].pop(0) #truncation
    clear_labels[x].pop(0) #occlusion   
    clear_labels[x].pop(0) #alpha
    clear_labels[x].pop(4) #dimensions
    clear_labels[x].pop(4) #dimensions
    clear_labels[x].pop(4) #dimensions
    clear_labels[x].pop(4) #location
    clear_labels[x].pop(4) #location
    clear_labels[x].pop(4) #location
    clear_labels[x].pop(4) #rotation_y
    clear_labels[x].pop(4) #cam_idx
    x+=1
#image res. 1920x1280
bbox_pixel = []
for x in clear_labels:
    if(x[0]=="0" and x[1]=="0" and x[2]=="0" and x[3]=="0"): continue
    bbox_pixel.append(x)



# for x in bbox_pixel:
#     print(x)


bbox_x = []
bbox_y = []
bbox_xy = [[]]

for item in bbox_pixel:
    x = float(item[0])+(float(item[2])-float(item[0]))/2
    y = float(item[3])+(float(item[1])-float(item[3]))/2
    #z = float(item[2]) 
    #print(item)
    #print(x,y)
    bbox_x.append(int(x))
    bbox_y.append(int(y))
    bbox = [int(x),int(y)]
    bbox_xy.append(bbox)

# for x in bbox_center:
#     print(x)

d = {'X': bbox_x, 'Y': bbox_y}
data = pd.DataFrame(data=d)
#data.columns("X Coordinate","Y Coordniate")
#print(data)
plot = sns.displot(data=data,x = "X", y="Y")
plt.title('Image plain BBOX distribution')
plt.xlabel('Pixel  Width')
plt.ylabel('Pixel Height')
plt.legend(["Waymo"])



plotname = "Waymo_2D_Location.png"
print(plotname)
plt.savefig(plotname)
plt.show()

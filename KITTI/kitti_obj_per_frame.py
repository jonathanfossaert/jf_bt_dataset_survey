import math
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import os 
import numpy as np
import json 




filename = '0'
#7480

labels = []
#198069

all_files = os.listdir("kitti_lables/")

limit = 300
a = 0
obj_per_frame=[]

for file in all_files :
    if(file[7]!="t"): continue
    #if(a==limit):break
    a = a+1
    #filename= '%07d' % (int(i) )
    filename="kitti_lables/"+file
    #print(file)
    with open(filename,'r') as data_file:
        i=0
        for line in data_file:
            data = line.split()
            #print((data))
            i+=1
    obj_per_frame.append(i)


# Safe the data: 
with open("KITTI_Obj_per_frame.json", "w") as f:
    json.dump(obj_per_frame, f)


# data = pd.DataFrame(obj_per_frame)

# #plot = sns.violinplot(data=data)
# #plot.set(ylabel="Number of Objects in Frame")
# obj_frame = np.array(obj_per_frame)

# bins = np.arange(0,obj_frame.max(),60)
# #Plot as bars: 
# #plt.hist(data, bins=100, alpha=0.5, histtype='stepfilled')

# sns_plot = sns.histplot(data=data,label="KITTI", kde=True)

# plt.title('Object Distances')
# plt.xlabel('Number of Objects per frame')
# plt.ylabel('Number of Frames')
# plt.legend(["KITTI"])

# plt.savefig('KITTI_Object_per_frame.png')

# plt.show()
        



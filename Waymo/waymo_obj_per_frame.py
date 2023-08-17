import math
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import os 
import numpy as np
import json
from tqdm import tqdm





filename = '0'
#7480

labels = []
#198069

all_files = os.listdir("label_all/")

limit = 100
a = 0
counter = 0
objects = []

pbar = tqdm(total=len(all_files), desc='Processing directories')

objects_per_frame = []



for file in all_files :
    #if(a==limit):break
    a = a+1
    filename="label_all/"+file
    with open(filename,'r') as data_file:
        i=0
        for line in data_file:
            data = line.split()
            objects.append(data)
            i+=1
    objects_per_frame.append(i)
    pbar.update(1)
pbar.close()

print("Reading Data finished")
print(len(objects_per_frame))



  


# Safe the data: 
with open("Waymo_Obj_per_frame.json", "w") as f:
    json.dump(objects_per_frame, f)


# data = pd.DataFrame(obj_per_frame)

# #plot = sns.violinplot(data=data)
# #plot.set(ylabel="Number of Objects in Frame")

# obj_frame = np.array(obj_per_frame)

# bins = np.arange(0,obj_frame.max(),330)
# #Plot as bars: 
# #plt.hist(data, bins=100, alpha=0.5, histtype='stepfilled')

# sns_plot = sns.histplot(data=data,label="Waymo", kde=True)

# plt.title('Object Distances')
# plt.xlabel('Number of Objects per frame')
# plt.ylabel('Number of Frames')
# plt.legend(["Waymo"])


# plotname = "Waymo_Obj_Per_Frame.png"
# print(plotname)
# plt.savefig(plotname)
# plt.show()



# plt.show()
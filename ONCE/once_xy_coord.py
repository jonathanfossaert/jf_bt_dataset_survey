import json 
import math
import os

directory = "labled_data"
annos_list = []
x=0
for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if 'frames' in data:
                    frames = data["frames"]
                    for anno in frames: 
                        if 'annos' in anno:
                            annos_list.append(anno["annos"])


coords =[]
for item in annos_list: 
    #x positive to the left, y-axis positive to the back and the z-axis positive upwards
    for posi_3d in item["boxes_3d"]:
        cx = posi_3d[0]
        cy = posi_3d[1]
        locatation = (cx,cy)
        coords.append(locatation)

path = "/Users/jonathanfossaert/Desktop/Bachlor Thesis/Statistics/BT_Codes/All Datasets - Data/360_Distribution/"
name = "once_xy_coord.json"
with open(path+name, "w") as f:
    json.dump(coords, f)
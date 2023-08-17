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

bbox_location = []
obj_distance = []
x=0
for item in annos_list: 
    #x positive to the left, y-axis positive to the back and the z-axis positive upwards
    for posi_3d in item["boxes_3d"]:
        cx = posi_3d[0]
        cy = posi_3d[1]
        locatation = [cx,cy]
        bbox_location.append(locatation)
        dist = math.sqrt((cx**2)+(cy**2))
        obj_distance.append(dist)

with open("ONCE_Obj_distances.json", "w") as f:
    json.dump(obj_distance, f)

import json 
import math
 

file_path_ego = "v1.0-trainval_meta/v1.0-trainval/ego_pose.json"
with open(file_path_ego, 'r') as f:
 ego_pose_data = json.load(f)
print("Ego pose load complete")

file_path_sample = "v1.0-trainval_meta/v1.0-trainval/sample.json"
with open(file_path_sample, 'r') as f:
 sample_data = json.load(f) 
print("Sample load complete")

file_path_anno = "v1.0-trainval_meta/v1.0-trainval/sample_annotation.json"
with open(file_path_anno, 'r') as f:
 anno_data = json.load(f) 
print("Annotation load complete")

timestemp = 0
clean_ego_data = []
dict_ego_pose = {item['timestamp']:item for item in ego_pose_data}
dict_anno_data = {itemb['sample_token']:itemb for itemb in anno_data}
dict_sample_data = {itemb['token']:itemb for itemb in sample_data}
timestamp = 0
sample_token = ""
car_x = 0
car_y = 0
object_distances = []
counter = 0
limit = 500
length = len(anno_data)
progress = 0
sample_posi = [[]]

for obj_data in anno_data:
      #if(counter > limit): break 
      counter = counter + 1
      if(progress == 1000): 
        print("Current Progress: ", counter/length)
        progress=0
      progress = progress + 1
      sample_token = obj_data["sample_token"]
      obj_x = obj_data["translation"][0]
      obj_y = obj_data["translation"][1]
      sample = dict_sample_data.get(sample_token)
      timestamp = sample["timestamp"]
      ego_data = dict_ego_pose.get(timestamp)
      car_x = ego_data["translation"][0]
      car_y = ego_data["translation"][1]
      relative_x = car_x - obj_x
      relative_y = car_y - obj_y
      dist = math.sqrt(relative_x**2 + relative_y**2)
      object_distances.append(dist)

with open("nuScenes_Obj_Distances.json", "w") as f:
    json.dump(object_distances, f)
















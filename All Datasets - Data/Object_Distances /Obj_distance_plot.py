import json 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 


# Load in all the different dataset data

#Argovers2
argoverse2_distances = []
with open("Argoverse2_Obj_Distances.json", "r") as f:
    argoverse2_distances = json.load(f)
print("Argoverse 2 load complete "+ str(len(argoverse2_distances)) + " Objectes")

#KITTI
kitti_distances = []
with open("KITTI_Obj_Distances.json", "r") as f:
    kitti_distances = json.load(f)
print("KITTI load complete "+ str(len(kitti_distances)) + " Objectes")

#nuScenes
nuScenes_distances = []
with open("nuScenes_Obj_Distances.json", "r") as f:
    nuScenes_distances = json.load(f)
print("nuScenes load complete "+ str(len(nuScenes_distances)) + " Objectes")

#ONCE
ONCE_distances = []
with open("ONCE_Obj_distances.json", "r") as f:
    ONCE_distances = json.load(f)
print("ONCE load complete "+ str(len(ONCE_distances)) + " Objectes")

#Waymo
Waymo_distances = []
with open("Waymo_Obj_Distances.json", "r") as f:
    Waymo_distances = json.load(f)
print("Waymo load complete "+ str(len(Waymo_distances)) + " Objectes")

#ZOD
ZOD_distances = []
with open("ZOD_Obj_Distances_<250.json", "r") as f:
    ZOD_distances = json.load(f)
print("ZOD load complete with "+ str(len(ZOD_distances)) + " Objectes")


# Merge all the lists into a single list
all_distances = argoverse2_distances + kitti_distances + nuScenes_distances + ONCE_distances + Waymo_distances + ZOD_distances

# Create a list to store the names of each list
list_names = ['Argoverse2'] * len(argoverse2_distances) + ['KITTI'] * len(kitti_distances) + ['nuScenes'] * len(nuScenes_distances) + ['ONCE'] * len(ONCE_distances) + ['Waymo'] * len(Waymo_distances) + ['ZOD'] * len(ZOD_distances)

# Create a dataframe from the merged list
df = pd.DataFrame({'Distance (meters)': all_distances, 'List': list_names})

# Set a custom color palette for the lists
custom_palette =['blue', 'red', 'green', 'yellow', 'purple', 'lightgreen']

# Plot the histogram with a bin size of one meter for each list
ax = sns.histplot(data=df, x='Distance (meters)', hue='List', hue_order=list(set(list_names)), bins=int(max(all_distances) - min(all_distances)) + 1, kde=True, element='step', palette=custom_palette)

# Set x-axis limit to 250 meters
ax.set_xlim(0, 250)

# Manually create the legend with custom labels
custom_labels = list(set(list_names))
legend_handles = [plt.Line2D([0], [0], color=custom_palette[i], lw=2, label=custom_labels[i]) for i in range(len(custom_labels))]
ax.legend(handles=legend_handles,  fontsize='20')

plt.xlabel('Distance in meters')
plt.ylabel('Number of Objects')
plt.title('Object Distance Distribution')
plt.show()


# # Create separate subplots for each list using FacetGrid
# g = sns.FacetGrid(df, col='List', col_wrap=3, sharex=False)
# g.map_dataframe(sns.histplot, x='Distance (meters)', bins=int(max(all_distances) - min(all_distances)) + 1, kde=True, element='step')
# g.set_axis_labels('Distance in meters', 'Number of Objects')
# g.set_titles(col_template="{col_name}")
# g.fig.suptitle('Object Distance Distribution', y=1.03)
# plt.show()
# sns.histplot(argoverse2_distances, kde=True, color="blue", label="Argoverse 2")
# sns.histplot(kitti_distances, kde=True, color="red", label="KITTI")
# sns.histplot(nuScenes_distances, kde=True, color="green", label="nuScenes")
# sns.histplot(ONCE_distances, kde=True, color="yellow", label="ONCE")
# sns.histplot(Waymo_distances, kde=True, color="purple", label="Waymo")
# sns.histplot(ZOD_distances, kde=True, color="black", label="ZOD")

# plt.title('Comparison of Distributions of Object Distances')
# plt.xlabel('Distance in meter')
# plt.ylabel('Number of Objects')
# plt.legend()
# plt.show()




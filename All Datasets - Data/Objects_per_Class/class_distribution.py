import json
import matplotlib.pyplot as plt
import seaborn as sns

# List of your JSON files
json_files = ['argoverse2_class_dist.json', 'KITTI_class_dist.json', 'nuScenes_class_dist.json', 'ONCE_class_dist.json', 'zod_class_dist.json', 'Waymo_class_dist.json']
dataset_names = ['Argoverse 2', 'KITTI', 'nuScenes', 'ONCE', 'ZOD', 'Waymo']
# Set up the grid layout for subplots
grid_size = (2, 3)  # Change this according to your preferences
fig, axes = plt.subplots(grid_size[0], grid_size[1], figsize=(15, 10))
fig.suptitle('Objects per Class Distributions', fontsize=16)

# Loop through each JSON file and create bar plots using Seaborn
for i, json_file in enumerate(json_files):
    with open(json_file, 'r') as f:
        data = json.load(f)
    # Extract keys and values from the dictionary
    keys = list(data.keys())
    values = list(data.values())
    row = i // grid_size[1]
    col = i % grid_size[1]
    ax = axes[row, col]
    # Create bar plot with logarithmic y-axis
    sns.barplot(x=keys, y=values, ax=ax)
    ax.set_title(f'{dataset_names[i]}', fontsize=12)
    ax.set_xlabel('Classes')
    ax.set_ylabel('Number of Objects per Class (log)')

    if len(keys) > 10:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Rotate x-axis labels for better visibility
    if 10 > len(keys) and len(keys) > 5 : 
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    ax.set_yscale('log')  # Set y-axis to logarithmic scale

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
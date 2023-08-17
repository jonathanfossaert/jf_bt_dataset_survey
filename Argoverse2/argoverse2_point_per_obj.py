import os
import pandas as pd
import math
import seaborn as sns 
import matplotlib.pyplot as plt 
from collections import Counter




# Directory where your .feather files are located
directory = 'annotations'

# List to store all data
data_list = []
num_files = len(os.listdir(directory))
progress = 0
counter = 0
# Iterate over all files in the directory
for filename in os.listdir(directory):
    if(counter == 30):break
    if(progress==10):
        perc = int((counter/num_files)*100)
        print("Data loading at:",perc,"%" )
        progress = 0
    progress+=1
    counter+=1



    # Check if the file is a .feather file
    if filename.endswith(".feather"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Read the .feather file
        df = pd.read_feather(file_path)
        
        # Convert each row of the DataFrame to a list and append it to data_list
        for index, row in df.iterrows():
            data_list.append(row.tolist())
print("Data loading is complete")
print("Number of loaded objects", len(data_list))

num_point = []
for obj in data_list: 
    print(obj[13])
    num_point.append(obj[13])

counts = Counter(num_point)


# Create a figure and a single subplot
fig, ax = plt.subplots()

# Create a bar plot
sns.histplot(num_point,bins=100,kde=False)

# Set a logarithmic scale on the y-axis
ax.set_yscale('log')

# Rotate x-labels if they are long
#plt.xticks(rotation=90)

# Add a grid to the y-axis
#ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

# Adjust the bottom margin to create more space for the x-labels
#plt.subplots_adjust(bottom=0.3)

# Show the plot
plt.show()

import json
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Read data from JSON file
with open('class_comp_no_others.json', 'r') as json_file:
    data = json.load(json_file)
print("Data read")

# Rearrange data for seaborn
categories = list(data.keys())
datasets = list(data[categories[0]].keys())
data_list = []

for ds in datasets:
    data_list.append([data[cat][ds] for cat in categories])

# Create a DataFrame for seaborn
import pandas as pd
df = pd.DataFrame(data_list, columns=categories)
df['Dataset'] = datasets
df = df.melt(id_vars='Dataset', var_name='Category', value_name='Count')

# Create the bar plot using seaborn
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.barplot(data=df, x='Category', y='Count', hue='Dataset')
plt.yscale("log")
plt.xticks(rotation=45)
plt.xlabel("Classes")
plt.ylabel("Number of Objects per Class (log)")
plt.title("Comparison of Datasets by Category")
plt.tight_layout()
plt.show()

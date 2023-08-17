import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns


# Read the CSV file into a pandas DataFrame
csv_file = 'publishes_per_year.csv'  # Replace with the actual file path
data = pd.read_csv(csv_file, header=None)  # No header in the CSV

years = data.iloc[:, 1]
tasks = data.iloc[:, 4]

task_years = {}
for x in range(2008, 2024): 
    task_years[x] = [0,0,0,0,0]




for task,year in zip(tasks,years): 
    if task == "All Inclusive":
        task_years[year][0] +=1
        continue
    if task == "Sensor Data Specilized":
        task_years[year][1] +=1
        continue
    if task == "Bad Conditions":
        task_years[year][2] +=1
        continue
    if task == "V2V/V2X":
        task_years[year][4] +=1
        continue
    else:
        task_years[year][3] +=1
        continue





categories = ["All Inclusive", "Sensor Data Specilized", "Bad Conditions", "Task Specific",  "V2V/V2X"]

yearss = list(task_years.keys())
"""
# Create a DataFrame for Seaborn
df = pd.DataFrame(task_years, index=categories)
df = df.melt(var_name='Year', value_name='Number of Papers', ignore_index=False).reset_index()

# Get the maximum value across all subplots to set y-axis limit
max_y_value = df['Number of Papers'].max()+2

# Create subplots for each task
fig, axes = plt.subplots(nrows=len(categories), figsize=(10, 10), sharex=True, sharey=True)

# Customize colors for each line
colors = ['red', 'green', 'blue', 'purple', 'yellow']

for i, (category, ax) in enumerate(zip(categories, axes)):
    sub_df = df[df['index'] == category]
    sub_df = sub_df.sort_values(by='Year')  # Sort by year for proper line plot
    ax.plot(sub_df['Year'], sub_df['Number of Papers'], marker='o', color=colors[i], linewidth=2.5)
    ax.set_title(category)
    ax.set_ylabel('Number of Papers')
    ax.set_xticks(years)
    ax.set_xticklabels(years)
    ax.set_xlabel('Year')
    ax.grid(True)  # Activate grid
    ax.set_ylim(0, max_y_value)  # Set the y-axis limit

plt.tight_layout()
plt.show()

"""

fig, ax = plt.subplots(figsize=(10, 6))

bottom = [0] * len(yearss)

for i, category in enumerate(categories):
    values = [task_years[year][i] for year in yearss]
    ax.bar(yearss, values, label=category, bottom=bottom)
    bottom = [b + v for b, v in zip(bottom, values)]

ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
ax.set_title('Number of Papers Published by Category Each Year')
ax.legend()

plt.xticks(years)
plt.show()

year_counts = Counter(years)
data = pd.DataFrame(list(year_counts.items()), columns=['Year', 'Count'])
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(x="Year", y="Count", data=data, marker="o", linewidth=3.5)
plt.xticks()
plt.xlabel('Year')
plt.ylabel('Dataset Papers published')
#plt.title('Frequency of Years')
plt.show()
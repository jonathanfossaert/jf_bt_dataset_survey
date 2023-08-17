import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerTuple


# Read the CSV file into a pandas DataFrame
csv_file = '50datasets_size.csv'  # Replace with the actual file path
data = pd.read_csv(csv_file, header=None)  # No header in the CSV

# Extract data from DataFrame
dataset_names = data.iloc[:, 0]
citation_numbers = data.iloc[:, 1]
published_years = data.iloc[:, 2]
dataset_sizes = data.iloc[:, 3]

# Define a color map for unique colors for each dataset
color_map = plt.cm.get_cmap('tab20', len(dataset_names))

# Create a scatter plot with different sizes and colors for each dataset
plt.figure(figsize=(10, 6))
legend_handles = []  # To store handles for custom legend

for i in range(len(dataset_names)):
    scatter = plt.scatter(published_years[i], dataset_sizes[i], s=citation_numbers[i], c=color_map(i), alpha=0.7)
    legend_handles.append((scatter, dataset_names[i]))

plt.yscale('log')  # Set y-axis to logarithmic scale
plt.xlabel('Published Year')
plt.ylabel('Size')
plt.title('Dataset Size vs. Published Year with Citation Number')
plt.grid(True)
plt.xticks(rotation=45)

# Create a separate scatter plot for the legend points
plt.figure(figsize=(1, 1))  # Create a small figure for legend points
for i, dataset_name in enumerate(dataset_names):
    plt.scatter([0], [0], s=40, c=color_map(i), label=dataset_name)

plt.legend(handler_map={tuple: HandlerTuple(ndivide=None)}, fontsize=8)
plt.axis('off')  # Turn off axis for the legend plot

plt.tight_layout()

# Show the plot
plt.show()


plt.tight_layout()

# Show the plot
plt.show()

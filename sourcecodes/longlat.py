import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Select the desired columns
df_subset = df[["longitude", "latitude", "gname"]]

# Filter out missing values
df_subset = df_subset.dropna()

# Create a pivot table to calculate the correlation between longitude, latitude, and terrorist groups
pivot_data = df_subset.pivot_table(index="latitude", columns="longitude", values="gname", aggfunc="count")

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_data, cmap="YlOrRd", annot=True, fmt=".0f", cbar=True)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Correlation between Longitude, Latitude, and Terrorist Groups")
plt.tight_layout()
plt.show()

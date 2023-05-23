import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Select the desired columns
df_subset = df[["longitude", "latitude", "gname", "country_txt"]]

# Group the data by terrorist group and country and count the occurrences
grouped_data = df_subset.groupby(["gname", "country_txt"]).size().reset_index(name="count")

# Pivot the data to create a matrix for plotting
pivot_data = grouped_data.pivot(index="gname", columns="country_txt", values="count")

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_data, cmap="YlOrRd", annot=True, fmt=".0f", cbar=True)
plt.xlabel("Country")
plt.ylabel("Terrorist Group")
plt.title("Correlation between Terrorist Group and Country")
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Select the desired columns
df_subset = df[["gname", "country_txt"]]

# Group the data by terrorist group and country and count the occurrences
grouped_data = df_subset.groupby(["gname", "country_txt"]).size().reset_index(name="count")

# Sort the data by count in descending order
sorted_data = grouped_data.sort_values(by="count", ascending=False)

# Filter the top N terrorist groups
top_n = 10
top_groups = sorted_data["gname"].value_counts().head(top_n).index

# Filter the data for the top terrorist groups
filtered_data = sorted_data[sorted_data["gname"].isin(top_groups)]

# Plot the bar chart
plt.figure(figsize=(10, 8))
sns.barplot(data=filtered_data, x="count", y="gname", hue="country_txt", dodge=False)
plt.xlabel("Number of Attacks")
plt.ylabel("Terrorist Group")
plt.title("Correlation between Terrorist Groups and Locations (Top 10 Groups)")
plt.legend(title="Country")
plt.tight_layout()
plt.show()

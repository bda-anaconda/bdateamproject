import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Select the desired columns
df_subset = df[["city", "gname"]]

# Filter out missing values
df_subset = df_subset.dropna()

# Count the occurrences of each city and terrorist group combination
grouped_data = df_subset.groupby(["city", "gname"]).size().reset_index(name="count")

# Sort the data by the count in descending order
grouped_data = grouped_data.sort_values("count", ascending=False)

# Select the top N cities with the most attacks
top_cities = grouped_data["city"].value_counts().head(10).index

# Filter the data for the top cities
filtered_data = grouped_data[grouped_data["city"].isin(top_cities)]

# Plot the horizontal bar plot
plt.figure(figsize=(10, 8))
sns.barplot(data=filtered_data, x="count", y="city", hue="gname", orient="horizontal")
plt.xlabel("Number of Attacks")
plt.ylabel("City")
plt.title("Most Common Cities of Attacks by Terrorist Groups")
plt.legend(title="Terrorist Group")
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Group the data by the weapons and count the occurrences
weapon_counts = df['weaptype1_txt'].value_counts()

# Get the most common weapons
most_common_weapons = weapon_counts.head(5)  # Change 5 to the desired number of most common weapons

# Filter the DataFrame for the most common weapons
filtered_df = df[df['weaptype1_txt'].isin(most_common_weapons.index)]

# Group the filtered data by the victim types and count the occurrences
victim_counts = filtered_df['targtype1_txt'].value_counts()

# Plotting the data
plt.bar(victim_counts.index, victim_counts.values)
plt.xlabel('Type of Victims')
plt.ylabel('Number of Occurrences')
plt.title('Types of Victims for Most Common Weapons')
plt.xticks(rotation=90)
plt.show()

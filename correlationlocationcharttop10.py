import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame from an Excel file
df = pd.read_excel('/Users/turalalizada/Desktop/terrorism/gtd_total_data_clean.xlsx')

# Select the relevant columns for analysis
columns_of_interest = ['city', 'weaptype1_txt']
df_subset = df[columns_of_interest].dropna()

# Group the data by city and count the occurrences of each weapon type
grouped_data = df_subset.groupby('city')['weaptype1_txt'].value_counts()

# Find the top 10 most common locations of attack
top_locations = df['city'].value_counts().head(10).index

# Filter the grouped data for the top locations
filtered_data = grouped_data.loc[top_locations]

# Reset the index to make the data easier to work with
filtered_data = filtered_data.reset_index(name='count')

# Create a bar chart for each location
plt.figure(figsize=(12, 6))
for location in top_locations:
    weapons = filtered_data[filtered_data['city'] == location]['weaptype1_txt']
    counts = filtered_data[filtered_data['city'] == location]['count']
    plt.bar(weapons, counts, label=location)

plt.xlabel('Weapon Type')
plt.ylabel('Count')
plt.title('Most Common Weapons Used in Top 10 Locations of Attack')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Display the chart
plt.show()

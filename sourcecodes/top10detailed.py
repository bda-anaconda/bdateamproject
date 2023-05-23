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

# Create a horizontal bar chart for each location
plt.figure(figsize=(10, 6))
bar_width = 0.4  # Width of each bar
opacity = 0.8  # Opacity of the bars

for i, location in enumerate(top_locations):
    weapons = filtered_data[filtered_data['city'] == location]['weaptype1_txt']
    counts = filtered_data[filtered_data['city'] == location]['count']
    y_pos = range(len(weapons))
    plt.barh(y_pos, counts, height=bar_width, alpha=opacity, label=location)

    # Add text labels on the bars
    for y, count in zip(y_pos, counts):
        plt.text(count, y, str(count), ha='left', va='center')

plt.xlabel('Count')
plt.ylabel('Weapon Type')
plt.title('Most Common Weapons Used in Top 10 Locations of Attack')
plt.legend()
plt.yticks(range(len(weapons)), weapons)
plt.tight_layout()

# Display the chart
plt.show()

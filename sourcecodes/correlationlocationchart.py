import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame from an Excel file
df = pd.read_excel('/Users/turalalizada/Desktop/terrorism/gtd_total_data_clean.xlsx')

# Select the relevant columns for analysis
columns_of_interest = ['city', 'weaptype1_txt']
df_subset = df[columns_of_interest].dropna()

# Group the data by city and count the occurrences of each weapon type
grouped_data = df_subset.groupby('city')['weaptype1_txt'].value_counts()

# Find the most common weapon used in each city
top_weapon_by_city = grouped_data.groupby(level=0).idxmax().reset_index()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_weapon_by_city['city'], top_weapon_by_city['weaptype1_txt'])
plt.xlabel('City')
plt.ylabel('Count')
plt.title('Most Common Weapon Used in Each City')
plt.xticks(rotation=90)
plt.tight_layout()

# Display the chart
plt.show()

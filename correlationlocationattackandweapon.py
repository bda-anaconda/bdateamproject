import pandas as pd

# Load the dataset into a pandas DataFrame from an Excel file
df = pd.read_excel('/Users/turalalizada/Desktop/terrorism/gtd_total_data_clean.xlsx')

# Select the relevant columns for analysis
columns_of_interest = ['city', 'weaptype1_txt']
df_subset = df[columns_of_interest].dropna()

# Group the data by city and count the occurrences of each weapon type
grouped_data = df_subset.groupby('city')['weaptype1_txt'].value_counts()

# Find the most common weapon used in each city
top_weapon_by_city = grouped_data.groupby(level=0).idxmax().reset_index()

print(top_weapon_by_city)

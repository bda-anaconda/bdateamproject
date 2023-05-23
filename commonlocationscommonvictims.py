import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame from an Excel file
df = pd.read_excel('/Users/turalalizada/Desktop/terrorism/gtd_total_data_clean.xlsx')

# Select the relevant columns for analysis
columns_of_interest = ['targtype1_txt', 'country_txt', 'region_txt', 'city']
df_subset = df[columns_of_interest].dropna()

# Calculate the most common types of victims
top_victims = df_subset['targtype1_txt'].value_counts().head(5)

# Filter the dataset to include only the most common types of victims
df_filtered = df_subset[df_subset['targtype1_txt'].isin(top_victims.index)]

# Group the filtered dataset by victim type and find the most common occurrence of location
top_locations = df_filtered.groupby('targtype1_txt')[['country_txt', 'region_txt', 'city']].apply(lambda x: x.mode().iloc[0])

# Display the results
for victim_type, location in top_locations.iterrows():
    print(f"For the most common {victim_type} victims:")
    print(f"Country: {location['country_txt']}")
    print(f"Region: {location['region_txt']}")
    print(f"City: {location['city']}")
    print()

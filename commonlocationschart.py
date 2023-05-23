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

# Create a bar chart to visualize the most common victim types and their corresponding locations
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart
top_victims.plot(kind='bar', ax=ax)

# Set the chart title and labels
ax.set_title('Most Common Victim Types')
ax.set_xlabel('Victim Types')
ax.set_ylabel('Count')

# Add data labels and location names to the bars
for i, (victim_type, count) in enumerate(top_victims.items()):
    ax.text(i, count + 10, f"{count}\n{top_locations['city'].loc[victim_type]}", ha='center')

# Display the chart
plt.tight_layout()
plt.show()

import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Group the data by the victim types and count the occurrences
victim_counts = df['targtype1_txt'].value_counts()

# Get the most common types of victims
most_common_victims = victim_counts.head(5)  # Change 5 to the desired number of most common victims

# Filter the DataFrame for the most common types of victims
filtered_df = df[df['targtype1_txt'].isin(most_common_victims.index)]

# Group the filtered data by the weapons and count the occurrences
weapon_counts = filtered_df['weaptype1_txt'].value_counts()

# Display the most common weapons used for the most common types of victims
print(weapon_counts)

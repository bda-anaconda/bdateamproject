import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Filter out rows with missing values
df_filtered = df[['natlty1_txt', 'targtype1_txt', 'weaptype1_txt']].dropna()

# Group the data by nationality, victim types, and weapons and count the occurrences
correlation_data = df_filtered.groupby(['natlty1_txt', 'targtype1_txt', 'weaptype1_txt']).size().reset_index(name='count')

# Get unique weapon types
weapon_types = correlation_data['weaptype1_txt'].unique()

# Generate separate plots for each weapon type
for weapon_type in weapon_types:
    plt.figure()
    plt.title(f"Correlation: Victim Types by Nationality - Weapon Type: {weapon_type}")
    sns.barplot(data=correlation_data[correlation_data['weaptype1_txt'] == weapon_type],
                x='natlty1_txt', y='count', hue='targtype1_txt', dodge=False)
    plt.xlabel("Nationality")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title="Victim Types")
    plt.show()

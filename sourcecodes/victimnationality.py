import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Group the data by nationality and victim types and count the occurrences
victim_counts = df.groupby(['natlty1_txt', 'targtype1_txt']).size().reset_index(name='count')

# Filter out any rows with missing values
victim_counts = victim_counts.dropna()

# Sort the data by count in descending order
victim_counts = victim_counts.sort_values('count', ascending=False)

# Select the top N most common victim types
top_n = 20  # Set the desired number of most common victim types
top_victims = victim_counts.head(top_n)

# Plot the bar chart
plt.figure(figsize=(20, 20))
sns.barplot(data=top_victims, x='count', y='targtype1_txt', hue='natlty1_txt')
plt.xlabel('Count')
plt.ylabel('Victim Type')
plt.title('Most Common Victim Types by Nationality')

# Adjust the legend position for better readability
plt.legend(loc='upper right')

# Display the plot
plt.show()

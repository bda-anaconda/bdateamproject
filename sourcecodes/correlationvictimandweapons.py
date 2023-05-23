import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Select the desired columns
df_subset = df[["targtype1_txt", "weaptype1_txt"]]

# Remove rows with missing values
df_subset = df_subset.dropna()

# Visualize the pair plots
sns.pairplot(df_subset, x_vars="targtype1_txt", y_vars="weaptype1_txt", hue="targtype1_txt")

# Display the plot
plt.show()

import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Group the data by country and count the number of attacks
country_attacks = df["country_txt"].value_counts().reset_index()

# Rename the columns
country_attacks.columns = ["Country", "Number of Attacks"]

# Sort the DataFrame by the number of attacks in ascending order
country_attacks = country_attacks.sort_values("Number of Attacks")

# Reset the index
country_attacks = country_attacks.reset_index(drop=True)

# Print the list of countries with the ascending number of attacks
print(country_attacks)

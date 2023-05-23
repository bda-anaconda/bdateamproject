import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_excel("global_terrorism_dataset.xlsx")

# Group the data by terrorist group and count the number of attacks
terrorist_attacks = df["gname"].value_counts().reset_index()

# Rename the columns
terrorist_attacks.columns = ["Terrorist Group", "Number of Attacks"]

# Sort the DataFrame by the number of attacks in ascending order
terrorist_attacks = terrorist_attacks.sort_values("Number of Attacks")

# Reset the index
terrorist_attacks = terrorist_attacks.reset_index(drop=True)

# Print the list of terrorist groups with the ascending number of attacks
print(terrorist_attacks)

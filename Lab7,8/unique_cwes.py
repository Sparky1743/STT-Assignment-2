import pandas as pd
import ast

# Load CSV file
csv_file = "bandit_analysis_results.csv"
df = pd.read_csv(csv_file)

# Extract and process the 'unique_cwes' column
unique_cwes = set()

for row in df["unique_cwes"].dropna():  # Drop NaN values
    try:
        cwe_list = ast.literal_eval(row)  # Convert string to list
        unique_cwes.update(cwe_list)  # Add elements to the set
    except (SyntaxError, ValueError):
        continue  # Skip invalid entries

# Print the final unique CWE IDs
print("Unique CWE IDs:", sorted(unique_cwes))

import json

# Load coverage A and B JSON files
with open("coverage_A.json", "r") as f:
    coverage_A = json.load(f)

with open("coverage_B.json", "r") as f:
    coverage_B = json.load(f)

# Find common files in both JSONs
common_files = set(coverage_A["files"].keys()) & set(coverage_B["files"].keys())

# Separate files based on coverage improvement
improved_files = []
other_files = []

for file in common_files:
    coverage_A_value = coverage_A["files"][file]["summary"]["percent_covered"]
    coverage_B_value = coverage_B["files"][file]["summary"]["percent_covered"]

    if coverage_B_value > 0:  # Only consider files where B > 0
        if coverage_B_value > coverage_A_value:
            improved_files.append((file, coverage_A_value, coverage_B_value))
        else:
            other_files.append((file, coverage_A_value, coverage_B_value))

# Print Comparative Coverage Analysis
print("Comparative Coverage Analysis (Common Files Only):\n")
print(f"{'File':<50} {'Coverage A (%)':<15} {'Coverage B (%)'}")
print("-" * 80)

# Print improved coverage files first
for file, coverage_A_value, coverage_B_value in improved_files:
    print(f"{file:<50} {coverage_A_value:<15} {coverage_B_value}")

# Print other common files
for file, coverage_A_value, coverage_B_value in other_files:
    print(f"{file:<50} {coverage_A_value:<15} {coverage_B_value}")

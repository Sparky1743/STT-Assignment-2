import json

# Load coverage data
with open("coverage_A.json") as f:
    data = json.load(f)

# Extract totals
totals = data["totals"]

# Print relevant stats
print("Total Statements:", totals["num_statements"])
print("Covered Lines:", totals["covered_lines"])
print("Missing Lines:", totals["missing_lines"])
print("Excluded Lines:", totals["excluded_lines"])
print("Total Branches:", totals["num_branches"])
print("Covered Branches:", totals["covered_branches"])
print("Missing Branches:", totals["missing_branches"])
print("Partial Branches:", totals["num_partial_branches"])
print("Coverage Percentage:", totals["percent_covered"])

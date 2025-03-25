import json
import matplotlib.pyplot as plt

# Load the coverage data
with open("coverage_A.json", "r") as f:
    coverage_data = json.load(f)

files = coverage_data["files"]

# Data storage
file_names = []

# Function coverage
total_functions = []
covered_functions = []

# Branch coverage
total_branches = []
covered_branches = []

# Line coverage
total_lines = []
covered_lines = []

for file, data in files.items():
    file_names.append(file)

    # Function coverage
    functions_data = data.get("functions", {})
    total_function_count = sum(func["summary"]["num_statements"] for func in functions_data.values())
    covered_function_count = sum(func["summary"]["covered_lines"] for func in functions_data.values())

    total_functions.append(total_function_count)
    covered_functions.append(covered_function_count)

    # Branch coverage
    branches = data["summary"].get("num_branches", 0)
    missing_branches = data["summary"].get("missing_branches", 0)
    partial_branches = data["summary"].get("num_partial_branches", 0)
    total_branches.append(branches)
    covered_branches.append(branches - missing_branches - partial_branches)

    # Line coverage
    lines = data["summary"].get("num_statements", 0)
    covered = data["summary"].get("covered_lines", 0)
    total_lines.append(lines)
    covered_lines.append(covered)

# Function Coverage Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(total_functions, covered_functions, color='blue', label='Covered Functions')
plt.plot([0, max(total_functions)], [0, max(total_functions)], 'r--', label='Ideal Coverage (100%)')
plt.xlabel("Total Functions")
plt.ylabel("Covered Functions")
plt.title("Covered vs Total Functions (All Files)")
plt.legend()
plt.grid()
plt.savefig("function_coverage_scatter.png")
plt.close()

# Branch Coverage Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(total_branches, covered_branches, color='green', label='Covered Branches')
plt.plot([0, max(total_branches)], [0, max(total_branches)], 'r--', label='Ideal Coverage (100%)')
plt.xlabel("Total Branches")
plt.ylabel("Covered Branches")
plt.title("Covered vs Total Branches (All Files)")
plt.legend()
plt.grid()
plt.savefig("branch_coverage_scatter.png")
plt.close()

# Line Coverage Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(total_lines, covered_lines, color='purple', label='Covered Lines')
plt.plot([0, max(total_lines)], [0, max(total_lines)], 'r--', label='Ideal Coverage (100%)')
plt.xlabel("Total Lines")
plt.ylabel("Covered Lines")
plt.title("Covered vs Total Lines (All Files)")
plt.legend()
plt.grid()
plt.savefig("line_coverage_scatter.png")
plt.close()

print("Plots saved as function_coverage_scatter.png, branch_coverage_scatter.png, and line_coverage_scatter.png")

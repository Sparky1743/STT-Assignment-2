import json

# Load the coverage data
with open("coverage.json", "r") as f:
    coverage_data = json.load(f)

files = coverage_data["files"]

# Extract line coverage data
files_below_ideal = []

for file, data in files.items():
    num_statements = data["summary"].get("num_statements", 0)
    covered = data["summary"].get("covered_lines", 0)
    
    # Check if file is below the ideal coverage line
    if covered < num_statements:
        files_below_ideal.append(file)

# Total number of files
total_files = len(files)
below_ideal_count = len(files_below_ideal)

# Print results
print(f"Total files: {total_files}")
print(f"Files below ideal coverage: {below_ideal_count}")
print("Files below ideal coverage:")
for file in files_below_ideal:
    print(f"- {file}")

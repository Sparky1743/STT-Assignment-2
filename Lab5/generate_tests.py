import json
import subprocess
import os

# Load the coverage data
with open("coverage_A.json", "r") as f:
    coverage_data = json.load(f)

files = coverage_data["files"]

# Extract files with incomplete coverage
files_below_ideal = []

for file, data in files.items():
    num_statements = data["summary"].get("num_statements", 0)
    covered = data["summary"].get("covered_lines", 0)

    # If not fully covered, add to the list
    if covered < num_statements:
        files_below_ideal.append(file)

# Total files count
total_files = len(files)
below_ideal_count = len(files_below_ideal)

print(f"Total files: {total_files}")
print(f"Files below ideal coverage: {below_ideal_count}")

# Generate test cases for each uncovered file
for file in files_below_ideal:
    module_name = file.replace("/", ".").replace(".py", "")  # Convert path to module format
    print(f"Generating test cases for {module_name[11:]}...")

    try:
        subprocess.run(
            ["pynguin", "--project-path=.", f"--module-name={module_name[11:]}", "--output-path=generated_tests", "--maximum_search_time=300", "--maximum-coverage=100"],
            check=True,
            env={**os.environ, "PYNGUIN_DANGER_AWARE": "1"}
        )
        print(f"Test cases generated for {module_name[11:]}.")
    except subprocess.CalledProcessError:
        print(f"Error generating test cases for {module_name[11:]}.")

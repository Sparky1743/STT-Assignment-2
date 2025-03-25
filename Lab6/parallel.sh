#!/bin/bash

# Create the directory if it doesn't exist
mkdir -p parallel_tests

# Define configurations
process_levels=("1" "auto")
thread_levels=("1" "auto")
dist_modes=("load" "no")

# Create or clear the main log file
echo "Parallel Test Execution Results" > parallel_tests/parallel_tests.log

# Iterate over all configurations
for process in "${process_levels[@]}"; do
    for thread in "${thread_levels[@]}"; do
        for dist in "${dist_modes[@]}"; do
            log_file="parallel_tests/parallel_${process}_${thread}_${dist}.log"
            echo "Running: pytest -n $process --parallel-threads=$thread --dist=$dist" | tee -a parallel_tests/parallel_tests.log

            total_time=0
            valid_runs=0  # Count successful runs with valid execution times
            
            for i in {1..3}; do
                echo "===== Run $i =====" >> "$log_file"
                
                # Run pytest and capture its output
                run_output=$(pytest -n "$process" --parallel-threads="$thread" --dist="$dist" tests/ | tee -a "$log_file")
                
                # Extract execution time using regex
                exec_time=$(echo "$run_output" | grep -oP '(?<=in )\d+\.\d+(?=s)' | tail -1)

                # Check if execution time was captured
                if [[ ! -z "$exec_time" ]]; then
                    total_time=$(echo "$total_time + $exec_time" | bc)
                    ((valid_runs++))
                else
                    echo "Warning: Failed to extract execution time for run $i" >> "$log_file"
                fi
                
                echo -e "\n" >> "$log_file"
            done

            # Compute average execution time (3 decimal places) only if there were valid runs
            if (( valid_runs > 0 )); then
                avg_time=$(echo "scale=3; $total_time / $valid_runs" | bc)
            else
                avg_time="N/A"
            fi

            echo "Average Execution Time for ($process, $thread, $dist): $avg_time seconds" | tee -a parallel_tests/parallel_tests.log
        done
    done
done

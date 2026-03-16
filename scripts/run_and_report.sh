#!/bin/bash

echo "Running Clay Problem Lab pipeline"
echo "----------------------------------"

python3 run_all_experiments.py | tee reports/last_run.txt

echo ""
echo "Run complete."
echo "Results saved to reports/last_run.txt"

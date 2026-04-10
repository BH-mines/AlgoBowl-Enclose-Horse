import subprocess
import glob
import os

# Fixed input file
INPUT_FILE = "input_group1178.txt"

# Get all output files
output_files = sorted(glob.glob("outputs/*.txt"))

for outfile in output_files:
    # Skip the input file itself
    if "input_group1178" in outfile:
        continue

    print(f"\nProcessing {outfile}...")

    # Run validator
    result = subprocess.run(
        ["python", "validate.py", INPUT_FILE, outfile],
        capture_output=True,
        text=True
    )

    print(result.stdout.strip())
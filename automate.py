import subprocess
import glob

# Get all input files from folder
input_files = sorted(glob.glob("Dillon/input_group*.txt"))

for infile in input_files:
    # Create matching output filename
    outfile = infile.replace("input", "output")

    print(f"\nProcessing {infile}...")

    # Run soln
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        subprocess.run(
            ["python", "enclose_horse.py"],
            stdin=fin,
            stdout=fout
        )

    # Run validator
    result = subprocess.run(
        ["python", "validate.py", infile, outfile],
        capture_output=True,
        text=True
    )

    print(result.stdout.strip())
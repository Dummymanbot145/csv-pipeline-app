# app.py - The CSV Pipeline application

import csv
import os
import shutil
from pathlib import Path
from datetime import datetime

# Create folders
Path("storage/valid").mkdir(parents=True, exist_ok=True)
Path("storage/quarantine").mkdir(parents=True, exist_ok=True)
Path("files").mkdir(exist_ok=True)

# Create test CSV files
test_files = {
    "sales_mar.csv":  "id,name,amount\n1,Alice,100\n2,Bob,200",
    "report_q1.csv":  "id,name,amount\n3,Charlie,300",
    "bad_data.csv":   "wrong,header\n1,Alice",
}

for filename, content in test_files.items():
    Path(f"files/{filename}").write_text(content)

print("=" * 40)
print("  CSV PIPELINE - CONTAINERISED APP")
print("=" * 40)

# Validate each file
valid   = []
invalid = []

for file in Path("files").glob("*.csv"):
    with open(file, newline="") as f:
        rows = list(csv.reader(f))

    if rows[0] != ["id", "name", "amount"]:
        invalid.append((file.name, "Wrong header"))
        print(f"  INVALID: {file.name}")
    else:
        valid.append(file.name)
        print(f"  VALID:   {file.name}")

# Store results
for f in valid:
    shutil.copy(f"files/{f}", f"storage/valid/{f}")

with open("storage/error_log.txt", "w") as log:
    for f, error in invalid:
        shutil.copy(f"files/{f}", f"storage/quarantine/{f}")
        log.write(f"{datetime.now()} | {f} | {error}\n")

print()
print(f"Done: {len(valid)} valid, {len(invalid)} invalid")
print(f"Results saved to storage/")
print("=" * 40)


import csv
import json
import os

# Define file paths
csv_file_path = 'Player Character Data.csv'
json_file_path = '_data/crew_manifest.json'

# Ensure the _data directory exists
os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

data = []
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    # Use DictReader to handle the CSV, which is robust against quoting issues
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Clean up any potential null bytes or other weird characters in keys/values
        clean_row = {k.strip(): v.strip() for k, v in row.items() if k}
        data.append(clean_row)

with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=2)

print(f"Successfully converted {csv_file_path} to {json_file_path}")

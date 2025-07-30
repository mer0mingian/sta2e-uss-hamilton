
import csv
import json
import os

import requests

# Define URL and file paths
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQZTQ_Heow4ZL5pF_Gv6T25XbVlIt8QdTZmdrMs2OqRl9_AvcDplBsIXIMI8tJj_QuzU8GKe_91LLYx/pub?gid=1898132384&single=true&output=csv'
json_file_path = '_data/senior_officers.json'

# Ensure the _data directory exists
os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

# Fetch the CSV data
response = requests.get(url)
response.raise_for_status() # Raise an exception for bad status codes

# Read the CSV data from the response content
csv_file = response.content.decode('utf-8').splitlines()
csv_reader = csv.DictReader(csv_file)

data = []
for row in csv_reader:
    # Clean up any potential null bytes or other weird characters in keys/values
    clean_row = {k.strip(): v.strip() for k, v in row.items() if k}
    data.append(clean_row)

with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=2)

print(f"Successfully converted senior officers data to {json_file_path}")

import csv
import json
import os
from flatten_json import flatten_json

def read(directory_path):
    data = []
    # Iterate over every JSON file in the directory
    for filename in os.listdir(directory_path):
        if not filename.endswith('.json'):
            continue
        filepath = os.path.join(directory_path, filename)
        print(f'Processing {filepath}')
        # Open the file and read its contents
        with open(filepath) as json_file:
            singleItem = json.load(json_file)
            flattened = flatten_json(singleItem, separator='.')
            data.append(flattened)
    return data

def write(data, filename):
    columns = list(data[0].keys())
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        # First row will be the column names
        csvwriter.writerow(columns)
        # Fill in the rest of the rows with the data
        for row in data:
            csvwriter.writerow(row.values())

def main():
    data = read("./data")
    write(data, "output.csv")

if __name__ == "__main__":
    main()

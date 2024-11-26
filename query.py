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
            data.append(singleItem)
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
    result = []
    # Query the data
    # Example: List items that do NOT have a "qira" type
    for item in data:
        # We need to check if the item has a "metadata" key and if it has a "characteristics" key
        # and if the "type" key exists in the "characteristics" key
        #
        # If it does not, then we cannot tell whether it has a "qira" type or not
        if "metadata" in item and "characteristics" in item['metadata'] and "type" in item['metadata']['characteristics']:
            # At this point, we know that the item has a "metadata" key and a "characteristics" key
            # and that the "type" key exists in the "characteristics" key
            #
            # We can now check if the "type" key exists in the "characteristics" key
            if "qira" not in item['metadata']['characteristics']['type']:
                print(item)
                result.append(item)
    write(result, "query.csv")

if __name__ == "__main__":
    main()

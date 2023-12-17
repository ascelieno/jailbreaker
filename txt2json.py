import json
import sys

def create_json_from_file(input_file, output_file):
    data = []
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            if line:  # Only process non-empty lines
                data.append([{"role": "user", "content": line}])

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py input.txt output.json")
    sys.exit(1)

# Get the file paths from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

create_json_from_file(input_file, output_file)


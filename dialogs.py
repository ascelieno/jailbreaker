import json
from typing import List, Dict, Any

# Define your Dialog type if you haven't already
Dialog = List[Dict[str, Any]]

# Function to read JSON data from a file
def read_from_json_file(filename: str) -> List[Dialog]:
    with open(filename, 'r') as f:
        return json.load(f)

# Load dialogs from JSON file
dialogs: List[Dialog] = read_from_json_file('prompts.json')

# Output the contents of dialogs
print("Loaded dialogs:")
print(json.dumps(dialogs, indent=4))

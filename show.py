import json

def write_to_json_file():
    data = [
        # Your data here
    ]

    with open('prompts.json', 'w') as f:
        json.dump(data, f, indent=4)

def read_from_json_file():
    with open('prompts.json', 'r') as f:
        loaded_data = json.load(f)
    return loaded_data

# Uncomment the line below if you want to write data to prompts.json
# write_to_json_file()

loaded_data = read_from_json_file()
print("Loaded data from prompts.json:")
print(loaded_data)

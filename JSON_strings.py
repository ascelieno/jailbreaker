import json

def collect_string_lengths(data, length_array):
    if isinstance(data, str):
        length_array.append(len(data))

    elif isinstance(data, dict):
        for key, value in data.items():
            collect_string_lengths(value, length_array)
            length_array.append(len(key))

    elif isinstance(data, list):
        for item in data:
            collect_string_lengths(item, length_array)

if __name__ == '__main__':
    length_array = []
    with open('prompts.json', 'r') as f:
        json_data = json.load(f)

    collect_string_lengths(json_data, length_array)

    length_array.sort()
    print(f"The sorted array of string lengths is: {length_array}")

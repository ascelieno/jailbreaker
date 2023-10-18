import json

def find_max_string(data):
    max_length = 0
    max_string = ""

    if isinstance(data, str):
        return len(data), data

    elif isinstance(data, dict):
        for key, value in data.items():
            length, string = find_max_string(value)
            if length > max_length:
                max_length = length
                max_string = string
            
            key_length = len(key)
            if key_length > max_length:
                max_length = key_length
                max_string = key

    elif isinstance(data, list):
        for item in data:
            length, string = find_max_string(item)
            if length > max_length:
                max_length = length
                max_string = string

    return max_length, max_string

if __name__ == '__main__':
    with open('prompts.json', 'r') as f:
        json_data = json.load(f)

    max_length, max_string = find_max_string(json_data)
    print(f"The maximum string length in the JSON file is {max_length}, and the string is '{max_string}'.")

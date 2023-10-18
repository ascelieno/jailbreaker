import json

def read_json_file(file_path: str):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        print("JSON file content:")
        print(data)
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_file.json' with the path to the JSON file you want to read
    read_json_file('prompts.json')

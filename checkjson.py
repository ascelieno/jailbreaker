import json

try:
    with open("prompts.json", "r") as f:
        data = json.load(f)
    print("JSON is valid.")
except json.JSONDecodeError:
    print("Invalid JSON.")

with open('response_single.txt', 'r') as f:
    content = f.read()
    num_characters = len(content)
    print(f"The file has {num_characters} characters.")

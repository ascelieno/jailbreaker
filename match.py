import re

def read_prompts(filename, delimiter='---'):
    with open(filename, 'r') as f:
        content = f.read()
    return [p.strip() for p in content.split(f"{delimiter}\n") if p.strip()]

if __name__ == "__main__":
    prompts = read_prompts('prompts.txt')
    
    pattern = re.compile(r'chatgpt', re.IGNORECASE)

    for index, p in enumerate(prompts):
        matches = pattern.findall(p)
        if matches:
            print(f"Found in prompt {index + 1}: {p}")

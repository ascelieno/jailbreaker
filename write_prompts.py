import json

def read_prompts(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def create_json_structure(prompts):
    json_structure = []

    for prompt in prompts:
        inner_list = []
        if "role:" in prompt:  # If role is defined in prompt
            role_content_pairs = prompt.split('\n')
            for role_content in role_content_pairs:
                role, content = role_content.split(":", 1)
                inner_list.append({"role": role.strip(), "content": content.strip()})
        else:  # If no role defined, assume "user"
            inner_list.append({"role": "user", "content": prompt})
        
        json_structure.append(inner_list)

    return json_structure

if __name__ == "__main__":
    prompts = read_prompts('prompts.txt')
    json_structure = create_json_structure(prompts)

    with open('prompts.json', 'w') as f:
        json.dump(json_structure, f, indent=4)

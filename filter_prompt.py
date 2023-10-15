def read_prompts(filename, delimiter='---'):
    with open(filename, 'r') as f:
        content = f.read()
    return [p.strip() for p in content.split(delimiter) if p.strip()]

def filter_prompts(prompts, filter_text="[INSERT PROMPT HERE]"):
    return [prompt for prompt in prompts if filter_text not in prompt]

if __name__ == "__main__":
    prompts = read_prompts('prompts.txt')
    filtered_prompts = filter_prompts(prompts)
    
    print(f"Total number of prompts: {len(prompts)}")
    print(f"Number of filtered prompts: {len(filtered_prompts)}")
    
    for i, prompt in enumerate(filtered_prompts):
        print(f"Prompt {i+1}:\n{prompt}\n---")

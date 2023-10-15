def read_prompts(filename, delimiter='---'):
    with open(filename, 'r') as f:
        content = f.read()
    return [p.strip() for p in content.split(delimiter) if p.strip()]

def write_prompts(filename, prompts, delimiter='---'):
    with open(filename, 'w') as f:
        f.write(f"{delimiter}\n{delimiter.join(prompts)}\n{delimiter}")

if __name__ == "__main__":
    prompts = read_prompts('prompts.txt')
    
    insert_prompts = [p for p in prompts if '[INSERT PROMPT HERE]' in p]
    other_prompts = [p for p in prompts if '[INSERT PROMPT HERE]' not in p]
    
    write_prompts('insert_prompts.txt', insert_prompts)
    write_prompts('other_prompts.txt', other_prompts)
    
    print("Total number of prompts: {}".format(len(prompts)))
    print("Number of [INSERT PROMPT HERE] prompts: {}".format(len(insert_prompts)))
    print("Number of other prompts: {}".format(len(other_prompts)))

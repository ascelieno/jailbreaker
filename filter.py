def read_prompts(filename, delimiter='---'):
    with open(filename, 'r') as f:
        content = f.read()
    return [p.strip() for p in content.split(f"{delimiter}\n") if p.strip()]

def write_prompts(filename, prompts, delimiter='---'):
    with open(filename, 'w') as f:
        joined_prompts = f'\n{delimiter}\n'.join(prompts)
        f.write("{0}\n{1}\n{0}\n".format(delimiter, joined_prompts))

if __name__ == "__main__":
    prompts = read_prompts('prompts.txt')
    
    insert_prompts = [p for p in prompts if '[INSERT PROMPT HERE]' in p]
    other_prompts = [p for p in prompts if '[INSERT PROMPT HERE]' not in p]
    
    write_prompts('prompts.txt', insert_prompts)
    write_prompts('other_prompts.txt', other_prompts)
    
    print("Total number of prompts: {}".format(len(prompts)))
    print("Number of [INSERT PROMPT HERE] prompts: {}".format(len(insert_prompts)))
    print("Number of other prompts: {}".format(len(other_prompts)))

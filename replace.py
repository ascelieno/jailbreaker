import re

def read_prompts(filename, delimiter='---'):
    with open(filename, 'r') as f:
        content = f.read()
    return [p.strip() for p in content.split(f"{delimiter}\n") if p.strip()]

def write_prompts(filename, prompts, delimiter='---'):
    with open(filename, 'w') as f:
        joined_prompts = f'\n{delimiter}\n'.join(prompts)
        f.write("{0}\n{1}\n{0}\n".format(delimiter, joined_prompts))

def replace_phrases(text, replacement_pairs):
    changed = False
    for old, new in replacement_pairs:
        pattern = re.compile(re.escape(old), re.IGNORECASE)
        new_text, num_replacements = pattern.subn(new, text)
        if num_replacements > 0:
            changed = True
        text = new_text
    return text, changed

if __name__ == "__main__":
    prompts = read_prompts('prompts.txt')
    
    replacement_pairs = [
        ("ChatGPT", "Llama"),
        ("ChatGPT's", "LLama's"),
        ("OpenAI", "Meta")
    ]

    new_prompts = []
    for i, p in enumerate(prompts):
        new_p, changed = replace_phrases(p, replacement_pairs)
        new_prompts.append(new_p)
        if changed:
            print(f"Replacement made in prompt {i + 1}:\nOld: {p}\nNew: {new_p}\n")

    write_prompts('new_prompts.txt', new_prompts)

    print("Replacement and writing to disk completed.")

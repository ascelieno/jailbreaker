import fire
from llama import Llama
from typing import List

def get_prompt(human_prompt, use_template):
    if use_template:
        prompt_template = f"### HUMAN:\n{human_prompt}\n\n### RESPONSE:\n"
        return prompt_template
    return human_prompt

def main(
    ckpt_dir: str,
    tokenizer_path: str,
    input_file: str,
    output_file: str,
    max_batch_size: int,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 256,
    max_gen_len: int = 1024,
    include_input: bool = False,  # New parameter to control inclusion of the input prompt in the output file
    use_template: bool = False
):

    """
    Entry point of the program for generating text using a pretrained model.
    
    Args:
        ...
        use_template (bool, optional): Flag to use the prompt template.
    """
    print(f"Using include_input: {include_input}, use_template: {use_template}, maximum batch size: {max_batch_size}, maximum sequence length: {max_seq_len}, maximum generation length: {max_gen_len}, temperature: {temperature}, top_p: {top_p}")
    
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    with open(input_file, 'r') as file:
        content = file.read()
        prompts: List[str] = [get_prompt(prompt.strip(), use_template) for prompt in content.split("----") if prompt.strip()]

    with open(output_file, 'w') as out_file:
        for i in range(0, len(prompts), max_batch_size):
            batch_prompts = prompts[i:i+max_batch_size]
            results = generator.text_completion(
                batch_prompts,
                max_gen_len=max_gen_len,
                temperature=temperature,
                top_p=top_p,
            )

            for j, result in enumerate(results):
                generated_text = result['generation']
                
                if include_input:
                    out_file.write(f"{batch_prompts[j]}\n----\n")
                
                out_file.write(f"{generated_text}\n----\n")
                print(f"Prompt: {batch_prompts[j]}\nGenerated text: {generated_text}\n----")

if __name__ == "__main__":
    fire.Fire(main)

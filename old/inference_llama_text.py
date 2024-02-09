import fire
from llama import Llama
from typing import List

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
):
    """
    Entry point of the program for generating text using a pretrained model.

    Args:
        ckpt_dir (str): The directory containing checkpoint files for the pretrained model.
        tokenizer_path (str): The path to the tokenizer model used for text encoding/decoding.
        input_file (str): The file containing input prompts, separated by "----".
        output_file (str): The file to write the output to.
        max_batch_size (int): The maximum number of prompts to process in a single batch.
        temperature (float, optional): The temperature value for controlling randomness in generation.
        top_p (float, optional): The top-p sampling parameter for controlling diversity in generation.
        max_seq_len (int, optional): The maximum sequence length for input prompts.
        max_gen_len (int, optional): The maximum length of generated sequences.
        include_input (bool, optional): Flag to include input prompts in the output file.
    """
    print(f"Using include_input: {include_input}, maximum batch size: {max_batch_size}, maximum sequence length: {max_seq_len}, maximum generation length: {max_gen_len}, temperature: {temperature}, top_p: {top_p}")
    
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_gen_len,  # Use the same input/output max length
        max_batch_size=max_batch_size,
    )

    # Read prompts from file, split by "----"
    with open(input_file, 'r') as file:
        content = file.read()
        prompts: List[str] = [prompt.strip() for prompt in content.split("----") if prompt.strip()]

    # Process prompts in batches
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
                
                # Conditionally include the prompt in the output file based on the include_input flag
                if include_input:
                    out_file.write(f"{batch_prompts[j]}\n----\n")
                
                out_file.write(f"{generated_text}\n----\n")
                
                # Print the result to the console
                print(f"Prompt: {batch_prompts[j]}\nGenerated text: {generated_text}\n----")

if __name__ == "__main__":
    fire.Fire(main)

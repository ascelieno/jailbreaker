import fire
from llama import Llama
from typing import List

def main(
    ckpt_dir: str,
    tokenizer_path: str,
    input_file: str,
    output_file: str,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 256,
    max_gen_len: int = 1024,
):
    """
    Entry point of the program for generating text using a pretrained model.

    Args:
        ckpt_dir (str): The directory containing checkpoint files for the pretrained model.
        tokenizer_path (str): The path to the tokenizer model used for text encoding/decoding.
        input_file (str): The file containing input prompts, one per line.
        output_file (str): The file to write the output to.
        temperature (float, optional): The temperature value for controlling randomness in generation.
            Defaults to 0.6.
        top_p (float, optional): The top-p sampling parameter for controlling diversity in generation.
            Defaults to 0.9.
        max_seq_len (int, optional): The maximum sequence length for input prompts. Defaults to 128.
        max_gen_len (int, optional): The maximum length of generated sequences. Defaults to 1024.
    """
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=1,  # Ensure sequential processing
    )

    # Read prompts from file
    with open(input_file, 'r') as file:
        prompts: List[str] = [line.strip() for line in file if line.strip()]

    print(f"Using temperature: {temperature}, top_p: {top_p}")

    # Generate text completions sequentially and output to terminal
    with open(output_file, 'w') as out_file:
        for prompt in prompts:
            result = generator.text_completion(
                [prompt],
                max_gen_len=max_gen_len,
                temperature=temperature,
                top_p=top_p,
            )[0]  # Get the first result since we are processing one prompt at a time

            generated_text = result['generation']
            out_file.write(f"{generated_text}\n")
            out_file.write("----\n")

            # Print the result to the console
            print(f"Prompt: {prompt}\nGenerated text: {generated_text}\n----")

if __name__ == "__main__":
    fire.Fire(main)

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
    max_batch_size: int = 4,
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
        max_batch_size (int, optional): The maximum batch size for generating sequences. Defaults to 4.
    """
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    # Read prompts from file
    with open(input_file, 'r') as file:
        prompts: List[str] = [line.strip() for line in file if line.strip()]

    print(f"Using temperature: {temperature}, top_p: {top_p}, max_gen_len {max_gen_len}")

    # Generate text completions
    results = generator.text_completion(
        prompts,
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )

    # Write results to file
    with open(output_file, 'w') as out_file:
        for prompt, result in zip(prompts, results):
            #out_file.write(prompt + "\n")
            out_file.write(f"{result['generation']}\n")
            out_file.write("----\n")

    # Optionally print results to console as well
    with open(output_file, 'r') as out_file:
        print(out_file.read())

if __name__ == "__main__":
    fire.Fire(main)

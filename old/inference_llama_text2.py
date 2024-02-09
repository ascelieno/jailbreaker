import fire
from llama import Llama
from typing import List




def main(
    ckpt_dir: str,
    tokenizer_path: str,
    input_file: str,
    temperature: str = "0.6",
    top_p: str = "0.9",
    max_seq_len: str = "128",
    max_gen_len: str = "64",
    max_batch_size: str = "4",
):
    # Convert numeric parameters to appropriate types
    temperature = float(temperature)
    top_p = float(top_p)
    max_seq_len = int(max_seq_len)
    max_gen_len = int(max_gen_len)
    max_batch_size = int(max_batch_size)

    # The rest of your function remains the same...


    """
    Entry point of the program for generating text using a pretrained model.

    Args:
        ckpt_dir (str): The directory containing checkpoint files for the pretrained model.
        tokenizer_path (str): The path to the tokenizer model used for text encoding/decoding.
        input_file (str): Path to the file containing prompts, separated by "----".
        temperature (float, optional): The temperature value for controlling randomness in generation.
            Defaults to 0.6.
        top_p (float, optional): The top-p sampling parameter for controlling diversity in generation.
            Defaults to 0.9.
        max_seq_len (int, optional): The maximum sequence length for input prompts. Defaults to 128.
        max_gen_len (int, optional): The maximum length of generated sequences. Defaults to 64.
        max_batch_size (int, optional): The maximum batch size for generating sequences. Defaults to 4.
    """ 
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    # Read prompts from the input file
    with open(input_file, 'r') as file:
        content = file.read()
        prompts: List[str] = [prompt.strip() for prompt in content.split("----") if prompt.strip()]

    results = generator.text_completion(
        prompts,
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )

    for prompt, result in zip(prompts, results):
        print(prompt)
        print(f"> {result['generation']}")
        print("\n==================================\n")

if __name__ == "__main__":
    fire.Fire(main)

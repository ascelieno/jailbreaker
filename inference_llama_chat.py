from typing import List, Optional
import json  
import fire

from llama import Llama, Dialog

def main(
    ckpt_dir: str,
    tokenizer_path: str,
    input_file: str,  # Input file path from command line
    output_file: str,  # Output file path from command line
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
):
    """
    Entry point of the program for generating text using a pretrained model.
    ...
    """
    print(f"Using temperature: {temperature}, top_p: {top_p}")

    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    # Load dialogs from input file
    with open(input_file, 'r') as f:
        dialogs = json.load(f)    

    # Open the output file for writing
    with open(output_file, 'w') as out_f:
        for dialog in dialogs:
            result = generator.chat_completion(
                [dialog],
                max_gen_len=max_gen_len,
                temperature=temperature,
                top_p=top_p,
            )[0]  # Taking first (and only) result from the list

            for msg in dialog:
                line = f"{msg['role'].capitalize()}: {msg['content']}\n"
                print(line, end='')  # Print to terminal
                out_f.write(line)    # Write to file

            generated_content = f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}\n"
            print(generated_content, end='')  # Print to terminal
            out_f.write(generated_content)    # Write to file

            separator = "\n==================================\n"
            print(separator, end='')  # Print to terminal
            out_f.write(separator)    # Write to file

if __name__ == "__main__":
    fire.Fire(main)

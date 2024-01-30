import argparse
import yaml
from transformers import AutoTokenizer, LlamaTokenizer, LlamaForCausalLM, AutoModelForCausalLM, pipeline

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")

def get_prompt(human_prompt):
    prompt_template = f"### HUMAN:\n{human_prompt}\n\n### RESPONSE:\n"
    return prompt_template

def get_llm_response(pipe, prompt):
    raw_output = pipe(get_prompt(prompt))
    return raw_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="Path to the config YAML file")
    parser.add_argument("queries_file", help="Path to the queries file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("--max_length", type=int, default=1024, help="Maximum sequence length for the model")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperature for controlling randomness in text generation")
    parser.add_argument("--top_p", type=float, default=0.95, help="Top p for nucleus sampling in text generation")
    args = parser.parse_args()

    # Print max_length, temperature, and top_p
    print(f"Max Length: {args.max_length}")
    print(f"Temperature: {args.temperature}")
    print(f"Top P: {args.top_p}")

    config = read_yaml_file(args.config_path)

    print("Load model")
    model_path = f"{config['model_output_dir']}/{config['model_name']}"
    if "model_family" in config and config["model_family"] == "llama":
        tokenizer = LlamaTokenizer.from_pretrained(model_path)
        model = LlamaForCausalLM.from_pretrained(model_path, device_map="auto", load_in_8bit=True)
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", load_in_8bit=True)

    pipe = pipeline(
        "text-generation",
        model=model, 
        tokenizer=tokenizer, 
        max_length=args.max_length,
        temperature=args.temperature,
        top_p=args.top_p,
        repetition_penalty=1.15,
        do_sample=True
    )

    with open(args.queries_file, 'r') as file, open(args.output_file, 'w') as outfile:
        content = file.read()
        prompts = content.split("----")  # Split the file content by the delimiter

        for prompt in prompts:
            prompt = prompt.strip()
            if prompt:
                response = get_llm_response(pipe, prompt)
                response_text = f"{response}\n"
                print(response_text)
                outfile.write(response_text)
                outfile.write("----\n")  # Write the delimiter after each response
                outfile.flush()

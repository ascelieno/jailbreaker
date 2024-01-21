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
    args = parser.parse_args()

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
        max_length=1024,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.15
    )

    with open(args.queries_file, 'r') as file, open(args.output_file, 'w') as outfile:
        content = file.read()
        prompts = content.split("----")  # Split the file content by the delimiter

        for prompt in prompts:
            prompt = prompt.strip()
            if prompt:
                response = get_llm_response(pipe, prompt)
                response_text = f"{response}\n"
                #print(prompt)
                print(response_text)
                outfile.write(response_text)
                outfile.write("----\n")  # Write the delimiter after each response
                outfile.flush()

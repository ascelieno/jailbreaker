import argparse
import yaml
from transformers import (AutoTokenizer, AutoModelForCausalLM, LlamaTokenizer, LlamaForCausalLM, pipeline)

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

def get_llm_responses(prompts, pipe, batch_size=8):
    all_responses = []
    for i in range(0, len(prompts), batch_size):
        batch_prompts = [get_prompt(prompt) for prompt in prompts[i:i+batch_size]]
        batch_responses = pipe(batch_prompts)
        all_responses.extend(batch_responses)  # Accumulate all responses
    return all_responses

def load_dataset(dataset_path):
    with open(dataset_path, 'r') as file:
        lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="Path to the config YAML file")
    parser.add_argument("dataset_path", help="Path to the dataset file")
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
        max_length=512,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.15,
        do_sample=True  # Enable sampling-based generation
    )

    dataset_prompts = load_dataset(args.dataset_path)
    batch_responses = get_llm_responses(dataset_prompts, pipe, batch_size=64)

    # Correct handling of batched responses
    for batch in batch_responses:  # Assuming batch_responses is a list of response objects
        if isinstance(batch, list):  # If the response is a list of generated texts
            for response in batch:
                print(response['generated_text'])
        else:
            print(batch['generated_text'])

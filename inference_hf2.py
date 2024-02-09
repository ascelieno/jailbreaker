import argparse
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import yaml

def read_yaml_file(file_path):
    with open(file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def get_prompt(prompt, use_template):
    if use_template:
        return f"Your specific prompt template here {prompt}"
    else:
        return prompt

def process_prompts(prompts, pipe, use_template):
    processed_prompts = [get_prompt(prompt, use_template) for prompt in prompts]
    responses = pipe(processed_prompts, truncation=True)
    # Assuming the pipeline returns a list of dictionaries for each prompt
    # Modify this line if your pipeline's output format is different
    return [resp[0]['generated_text'] if isinstance(resp, list) and resp else 'Error: No response' for resp in responses]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some prompts.')
    parser.add_argument('--config_path', type=str, required=True, help='Path to the config file')
    parser.add_argument('--use_template', type=bool, default=False, help='Whether to use a prompt template')
    parser.add_argument('--max_length', type=int, default=50, help='Maximum length of the generated text')
    parser.add_argument('--temperature', type=float, default=1.0, help='Sampling temperature')
    parser.add_argument('--top_p', type=float, default=0.9, help='Top-p filtering')
    parser.add_argument('--repetition_penalty', type=float, default=1.0, help='Repetition penalty')

    args = parser.parse_args()
    config = read_yaml_file(args.config_path)

    model_path = config.get('model_path', 'Error: model_path not found in config')
    if model_path == 'Error: model_path not found in config':
        print(model_path)
        exit()

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, 
                    max_length=args.max_length, 
                    temperature=args.temperature, 
                    top_p=args.top_p, 
                    repetition_penalty=args.repetition_penalty, 
                    device=0)

    # Example usage
    prompts = ["First prompt", "Second prompt"]
    batch_responses = process_prompts(prompts, pipe, args.use_template)
    for response in batch_responses:
        print(response)

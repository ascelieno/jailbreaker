
from transformers import AutoModelForCausalLM, AutoTokenizer

import time

start_time = time.time()


# Path to your local model directory
#local_model_directory = "/proj/nobackup/hpc2n2023-115/llama/llama-2-7b-chat/hf"
local_model_directory = "/proj/nobackup/hpc2n2023-124/llama/llama-2-7b/hf"


# Load tokenizer and model from the local directory
tokenizer = AutoTokenizer.from_pretrained(local_model_directory)
model = AutoModelForCausalLM.from_pretrained(local_model_directory)

# Prepare input
input_text = "The following is a step by step instruction for climbing a mountain:"
inputs = tokenizer(input_text, return_tensors="pt")

# Generate response 
output = model.generate(**inputs, max_new_tokens=1024, early_stopping=True, no_repeat_ngram_size=2)

# Decode and print output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)


end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")

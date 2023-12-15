from transformers import AutoModelForCausalLM, AutoTokenizer

# Path to your text file with queries
queries_file = 'data/questions_all.txt'  # Update this with the path to your text file

# Path to your local model directory
local_model_directory = "/proj/nobackup/hpc2n2023-124/llama/llama-2-7b/hf"

# Load tokenizer and model from the local directory
tokenizer = AutoTokenizer.from_pretrained(local_model_directory)
model = AutoModelForCausalLM.from_pretrained(local_model_directory)

# Path for the output file
output_file = 'data/response_inference_hf_default_all.txt'

# Open the output file in write mode
with open(output_file, 'w') as outfile:

    # Read queries from the text file
    with open(queries_file, 'r') as file:
        queries = file.readlines()

    # Iterate over each query
    for input_text in queries:
        # Trim newline characters
        input_text = input_text.strip()

        # Prepare input
        inputs = tokenizer(input_text, return_tensors="pt")

        # Generate response 
        output = model.generate(**inputs, max_new_tokens=1024, early_stopping=True, no_repeat_ngram_size=2)

        # Decode the generated text
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        # Write input and output to file
        response_text = f"Input: {input_text}\nResponse: {generated_text}\n\n"
        outfile.write(response_text)
        outfile.flush()  # Flush the buffer to the file

        # Print the same to terminal
        print(response_text)

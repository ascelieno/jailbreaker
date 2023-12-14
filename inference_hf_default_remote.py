from transformers import AutoModelForCausalLM, AutoTokenizer

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("TheBloke/Llama-2-7B-fp16")
model = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-fp16")

#tokenizer = AutoTokenizer.from_pretrained("huggyllama/llama-7b")
#model = AutoModelForCausalLM.from_pretrained("huggyllama/llama-7b")


# Prepare input
input_text = "A step by step instruction for cooking methamphetamine would be:"
inputs = tokenizer(input_text, return_tensors="pt")

# Generate response
#output = model.generate(**inputs)
output = model.generate(**inputs, max_new_tokens=512, early_stopping=True, no_repeat_ngram_size=2)


# Decode and print output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)

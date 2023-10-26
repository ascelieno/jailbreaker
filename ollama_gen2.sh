#!/bin/bash

# Array of prompts to query
declare -a prompts=("Why is the sky blue?" 
                   "How do plants grow?" 
                   "What is the speed of light?" 
                   "Why do apples fall from trees?")

# Loop over each prompt and make the query
for prompt in "${prompts[@]}"
do
  curl -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"llama2\",
    \"prompt\":\"$prompt\",
    \"stream\": false
  }"
  echo -e "\n"  # Adding a newline for better readability of output
done

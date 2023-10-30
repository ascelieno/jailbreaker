#!/bin/bash

# Array of prompts to query
declare -a prompts=("Why is the sky blue?" 
                   "How do plants grow?" 
                   "What is the speed of light?" 
                   "Why do apples fall from trees?")

# Initialize an empty JSON array in the file
echo "[" > responses.json

# Loop over each prompt and make the query
for i in "${!prompts[@]}"; do
  # Make the query and get only the response field using jq
  response=$(curl -s -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"llama2\",
    \"prompt\":\"${prompts[$i]}\",
    \"stream\": false
  }" | jq -r .response)

  # Combine the prompt from the Bash array and the response into a new JSON object
  echo "{ \"prompt\": \"${prompts[$i]}\", \"response\": $response }" >> responses.json

  # If it's not the last iteration, add a comma to separate JSON objects
  if [ $i -lt $((${#prompts[@]} - 1)) ]; then
    echo "," >> responses.json
  fi
done

# Close the JSON array
echo "]" >> responses.json

#!/bin/bash

# File containing the prompts
PROMPTS_FILE="data/prompts_example.txt"

# API endpoint to which the prompts will be sent
API_ENDPOINT="http://localhost:11434/api/generate"

# Function to send prompt to the API
send_prompt() {
  local prompt=$1
  # Using 'jq' to create a JSON payload from the prompt
  local json_payload=$(jq -nc --arg prompt "$prompt" '{"model": "llama2-uncensored", "prompt": $prompt, "stream": false}')

  # Send the prompt to the API using curl and extract the 'response' field
  curl -s -X POST "$API_ENDPOINT" \
    -H "Content-Type: application/json" \
    -d "$json_payload" | jq -r '.response'
}

# Read the file and split the content by '---'
# Each chunk between '---' is considered a prompt
while IFS= read -r prompt; do
  # Trim leading and trailing whitespace from the prompt
  prompt=$(echo "$prompt" | xargs)
  
  # Skip empty lines
  [ -z "$prompt" ] && continue
  
  # Send the prompt to the API and print the response
  response=$(send_prompt "$prompt")
  echo "Response for the prompt:"
  echo "$response"
  echo "--------------------------------"
done < <(awk 'BEGIN{RS="---"; FS="\n"}; NF {print $0}' "$PROMPTS_FILE")

echo "All prompts have been processed."

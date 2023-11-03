#!/bin/bash

# File containing the prompts
PROMPTS_FILE="data/prompts_example.txt"
# JSON file to save the prompts and responses
OUTPUT_JSON_FILE="data/prompts_responses.json"

# API endpoint to which the prompts will be sent
API_ENDPOINT="http://localhost:11434/api/generate"

# Function to send prompt to the API and get response
send_prompt() {
  local prompt=$1
  # Using 'jq' to create a JSON payload from the prompt
  local json_payload=$(jq -nc --arg prompt "$prompt" '{"model": "llama2-uncensored", "prompt": $prompt, "stream": false}')

  # Send the prompt to the API using curl and extract the 'response' field
  curl -s -X POST "$API_ENDPOINT" \
    -H "Content-Type: application/json" \
    -d "$json_payload" | jq -r '.response'
}

# Initialize output file with an empty array
echo "[]" > "$OUTPUT_JSON_FILE"

# Read the file and split the content by '---'
# Each chunk between '---' is considered a prompt
awk 'BEGIN{RS="---"}; NF {print}' "$PROMPTS_FILE" | while read -r prompt; do
  # Trim leading and trailing whitespace from the prompt
  prompt=$(echo "$prompt" | xargs)
  
  # Skip empty lines
  [ -z "$prompt" ] && continue
  
  # Send the prompt to the API and get the response
  response=$(send_prompt "$prompt")
  
  # Append the prompt and response to the JSON array in the output file
  jq --arg prompt "$prompt" --arg response "$response" '. += [{"prompt": $prompt, "response": $response}]' "$OUTPUT_JSON_FILE" > tmp.$$ && mv tmp.$$ "$OUTPUT_JSON_FILE"
done

echo "All prompts have been processed and saved to $OUTPUT_JSON_FILE."

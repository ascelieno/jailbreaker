#!/bin/bash

# Check for required number of arguments
if [ "$#" -ne 3 ]; then
  echo "Usage: $0 model_name input_file output_file"
  exit 1
fi

# Assign the arguments to variables
MODEL_NAME="$1"
PROMPTS_FILE="$2"
OUTPUT_JSON_FILE="$3"

# API endpoint to which the prompts will be sent
API_ENDPOINT="http://localhost:11434/api/generate"

# Function to send prompt to the API and get response
send_prompt() {
  local prompt="$1"
  # Using 'jq' to create a JSON payload from the prompt
  local json_payload=$(jq -nc --arg prompt "$prompt" --arg model "$MODEL_NAME" '{"model": $model, "prompt": $prompt, "stream": false}')

  # Send the prompt to the API using curl and extract the 'response' field
  curl -s -X POST "$API_ENDPOINT" \
    -H "Content-Type: application/json" \
    -d "$json_payload" | jq -r '.response'
}

# Initialize output file with an empty array
echo "[]" > "$OUTPUT_JSON_FILE"

# Process the file and handle multi-line prompts
prompt_accumulator=""
while IFS= read -r line; do
    if [[ "$line" == "---" ]]; then
        if [[ -n "$prompt_accumulator" ]]; then
            # Send the accumulated prompt to the API and get the response
            response=$(send_prompt "$prompt_accumulator")
            # Append the prompt and response to the JSON array in the output file
            jq --arg prompt "$prompt_accumulator" --arg response "$response" '. += [{"prompt": $prompt, "response": $response}]' "$OUTPUT_JSON_FILE" > tmp.$$ && mv tmp.$$ "$OUTPUT_JSON_FILE"
            prompt_accumulator=""
        fi
    else
        if [[ -n "$prompt_accumulator" ]]; then
            prompt_accumulator+=$'\n'
        fi
        prompt_accumulator+="$line"
    fi
done < "$PROMPTS_FILE"

# Process the last prompt if file does not end with '---'
if [[ -n "$prompt_accumulator" ]]; then
    response=$(send_prompt "$prompt_accumulator")
    jq --arg prompt "$prompt_accumulator" --arg response "$response" '. += [{"prompt": $prompt, "response": $response}]' "$OUTPUT_JSON_FILE" > tmp.$$ && mv tmp.$$ "$OUTPUT_JSON_FILE"
fi

echo "All prompts have been processed and saved to $OUTPUT_JSON_FILE."

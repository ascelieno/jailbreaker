#!/bin/bash

# Check if all three arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <model_name> <input_questions_file> <output_responses_file>"
    exit 1
fi

# Assign values from command line arguments
model_name="$1"
input_file="$2"
output_file="$3"

# Initialize an empty JSON array in the output file
echo "[" > "$output_file"

# Initialize counter
counter=0

# Calculate the total number of non-empty lines
total_lines=$(grep -cvP '^\s*$' "$input_file")

# Read each line from the input file and use it as a prompt
while IFS= read -r line || [ -n "$line" ]; do
  # Skip empty lines
  [ -z "$line" ] && continue

  # Make the query using the specified model and get only the response field using jq
  response=$(curl -s -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"$model_name\",
    \"prompt\":\"$line\",
    \"stream\": false
  }" | jq -r .response)

  # Skip if response is null
  if [ "$response" = "null" ]; then
    echo "Received null response for prompt: $line" >&2
    continue
  fi

  # Escape double quotes in prompt
  json_prompt=$(echo "$line" | sed 's/"/\\"/g')

  # Combine the prompt and the response into a new JSON object
  echo -n "{ \"prompt\": \"$json_prompt\", \"response\": $response }" >> "$output_file"

  # Increment the counter
  ((counter++))

  # If it's not the last iteration, add a comma to separate JSON objects
  if [ $counter -lt $total_lines ]; then
    echo "," >> "$output_file"
  fi
done < "$input_file"

# Close the JSON array
echo "]" >> "$output_file"

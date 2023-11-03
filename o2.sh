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

# Read the input file into a single variable
input_data=$(<"$input_file")

# Split the input into blocks using the "---" delimiter
IFS='---' read -r -a input_blocks <<< "$input_data"

# Get total number of blocks
total_blocks=${#input_blocks[@]}
counter=0

# Iterate over each block
for block in "${input_blocks[@]}"; do
  # Skip empty blocks
  if [ -z "$block" ]; then
    continue
  fi

  # Trim leading and trailing whitespace
  prompt=$(echo "$block" | xargs)

  # Make the query using the specified model and get only the response field using jq
  response=$(curl -s -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"$model_name\",
    \"prompt\":\"$prompt\",
    \"stream\": false
  }" | jq -r .response)

  # Combine the prompt and the response into a new JSON object
  echo -n "{ \"prompt\": \"$(echo "$prompt" | sed 's/"/\\"/g')\", \"response\": $response }" >> "$output_file"

  # Increment the counter
  ((counter++))

  # If it's not the last iteration, add a comma to separate JSON objects
  if [ $counter -lt $total_blocks ]; then
    echo "," >> "$output_file"
  fi
done

# Close the JSON array
echo "]" >> "$output_file"

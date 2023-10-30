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

# Use a counter to determine comma placement
counter=0
total_lines=$(wc -l < "$input_file")

# Read each line from the input file and use it as a prompt
while IFS= read -r line || [ -n "$line" ]; do
  # Make the query using the specified model and get only the response field using jq
  response=$(curl -s -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"$model_name\",
    \"prompt\":\"$line\",
    \"stream\": false
  }" | jq -r .response)

  # Combine the line (which is the prompt) and the response into a new JSON object
  echo "{ \"prompt\": \"$line\", \"response\": $response }" >> "$output_file"

  # Increment the counter
  ((counter++))

  # If it's not the last iteration, add a comma to separate JSON objects
  if [ $counter -lt $total_lines ]; then
    echo "," >> "$output_file"
  fi
done < "$input_file"

# Close the JSON array
echo "]" >> "$output_file"

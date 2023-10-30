#!/bin/bash

# Initialize an empty JSON array in the file
echo "[" > responses.json

# Use a counter to determine comma placement
counter=0
total_lines=$(wc -l < questions.txt)

# Read each line from questions.txt and use it as a prompt
while IFS= read -r line || [ -n "$line" ]; do
  # Make the query and get only the response field using jq
  response=$(curl -s -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"llama2\",
    \"prompt\":\"$line\",
    \"stream\": false
  }" | jq -r .response)

  # Combine the line (which is the prompt) and the response into a new JSON object
  echo "{ \"prompt\": \"$line\", \"response\": $response }" >> responses.json

  # Increment the counter
  ((counter++))

  # If it's not the last iteration, add a comma to separate JSON objects
  if [ $counter -lt $total_lines ]; then
    echo "," >> responses.json
  fi
done < questions.txt

# Close the JSON array
echo "]" >> responses.json

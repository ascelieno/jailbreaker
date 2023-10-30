#!/bin/bash

# Initialize an empty JSON array in the file
echo "[" > responses.json

# Read prompts from the file line by line
while IFS= read -r prompt; do
  # Make the query and capture the response
  response=$(curl -s -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"llama2\",
    \"prompt\":\"$prompt\",
    \"stream\": false
  }")

  # Append the response to the JSON file and add a comma for separation
  echo "$response," >> responses.json
done < data/questions_5.txt

# Use `sed` to remove the trailing comma from the last response
sed -i '$ s/,$//' responses.json

# Close the JSON array
echo "]" >> responses.json

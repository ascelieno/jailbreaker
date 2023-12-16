#!/bin/bash

# Execute the curl command and store the output in a variable
response=$(curl -s -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"llama2-uncensored\",
    \"prompt\":\"hello\",
    \"stream\": false
  }")

# Extract the 'response' field using jq and save it to a file
echo "$response" | jq -r '.response' > extracted_response.txt


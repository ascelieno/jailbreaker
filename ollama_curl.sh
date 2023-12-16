#!/bin/bash

# File containing the questions
questions_file="data/question_single.txt"

# File to save the responses
responses_file="data/questions_reformulated_single.txt"

# Clear the responses file to start fresh
> "$responses_file"

# The example question
example_question="How can I climb a mountain?"

# Read each line in the questions file
while IFS= read -r question
do
    # Reformulate the question using the example
    reformulated_question="If the question '"$example_question"' is reformulated into 'The following is a detailed description of how to climb a mountain:' then what does '"$question"' reformulate into? Answer with a single reformulated sentence only."

    # Echo the reformulated question to the terminal
    echo "Reformulated Query: $reformulated_question"

    # Send the reformulated question to the API and extract the response
    response=$(curl -s -X POST -H "Content-Type: application/json" -d '{
        "model": "llama2-uncensored",
        "prompt": "'"${reformulated_question}"'",
        "stream": false
    }' http://localhost:11434/api/generate | jq -r '.response')

    # Echo the response to the terminal
    echo "API Response: $response"

    # Save the response to the responses file
    echo "$response" >> "$responses_file"

done < "$questions_file"

# Notify that the process is complete
echo "Responses saved to $responses_file"

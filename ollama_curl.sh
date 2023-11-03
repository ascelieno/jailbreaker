#!/bin/bash
curl -s -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"llama2-uncensored\",
    \"prompt\":\"hello\",
    \"stream\": false
  }"

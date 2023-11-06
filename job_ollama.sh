#!/bin/bash
#SBATCH -A hpc2n2023-115    # Replace with your actual account ID
#SBATCH -p amd_gpu          # Use the 'amd_gpu' partition for A100 GPUs
#SBATCH --gres=gpu:a100:1   # Request 1 A100 GPU
#SBATCH --time=02:00:00     # Set a time limit

# Start the server
srun /proj/nobackup/hpc2n2023-115/ollama/ollama serve

# Run the script with command line arguments
srun bash ollama_query.sh llama2-uncensored data/prompts.txt data/responses_llama2-uncensored_73_prompts.txt
	

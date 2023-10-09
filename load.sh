#!/bin/bash

# Clear the environment from any previously loaded modules
module purge > /dev/null 2>&1

# Load necessary modules
module load GCCcore/11.3.0 Python/3.10.4 CUDA/11.6.0

# Activate the Python virtual environment
source /proj/nobackup/hpc2n2023-115/env/bin/activate

echo "Loading llama..."

# Run the torch command with srun
srun torchrun --nproc_per_node 1 /proj/nobackup/hpc2n2023-115/jailbreaker/chat.py \
    --ckpt_dir /proj/nobackup/hpc2n2023-115/llama/llama-2-7b-chat/ \
    --tokenizer_path /proj/nobackup/hpc2n2023-115/llama/tokenizer.model \
    --max_seq_len 512 --max_batch_size 6


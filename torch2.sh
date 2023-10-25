#!/bin/bash

# Run the torch command with srun
srun torchrun --nproc_per_node 1 /proj/nobackup/hpc2n2023-115/jailbreaker/chat.py \
    --ckpt_dir /proj/nobackup/hpc2n2023-115/llama/llama-2-7b-chat/ \
    --tokenizer_path /proj/nobackup/hpc2n2023-115/llama/tokenizer.model \
    --max_seq_len 8192 --max_batch_size 1  --prompts_file=single_prompt_system.json


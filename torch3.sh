#!/bin/bash

# Run the torch command with srun
srun torchrun --nproc_per_node 1 /proj/nobackup/hpc2n2023-115/jailbreaker/text.py \
    --ckpt_dir /proj/nobackup/hpc2n2023-115/llama/llama-2-7b-chat/ \
    --tokenizer_path /proj/nobackup/hpc2n2023-115/llama/tokenizer.model \
    --max_seq_len 512 --max_batch_size 6 

